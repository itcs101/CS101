-- hsbc.lua — Combined pandoc filter:
--   1. Strip "N.", "N.N." prefixes from headings (方案C: avoid double-numbering)
--   2. Make title H1 unnumbered
--   3. Auto-number Figures (图 N) and Tables (表 N)

local fig_count = 0
local tbl_count = 0
local last_heading = ""
local first_h1_seen = false

-- ── Heading processing ──
function Header(el)
  local inlines = el.content
  if #inlines == 0 then return el end

  -- Make the very first H1 (the report title) unnumbered
  if el.level == 1 and not first_h1_seen then
    first_h1_seen = true
    local full_text = pandoc.utils.stringify(el)
    -- If it looks like a title (contains "HSBC" or no "N." prefix)
    if full_text:match("HSBC") or not full_text:match("^%d+%.") then
      el.classes:insert("unnumbered")
      return el
    end
  end

  -- Get text of first inline
  local first_text = pandoc.utils.stringify(inlines[1])

  -- Strip hierarchical number prefix: "1." "1.1" "1.1.1" etc.
  local stripped = first_text:gsub("^%d+%.%d+%.%d+%.?", "")
  if stripped == first_text then
    stripped = first_text:gsub("^%d+%.%d+%.?", "")
  end
  if stripped == first_text then
    stripped = first_text:gsub("^%d+%.?", "")
  end

  if stripped ~= first_text then
    if stripped == "" then
      table.remove(inlines, 1)
      if #inlines > 0 and inlines[1].t == "Space" then
        table.remove(inlines, 1)
      end
    else
      inlines[1] = pandoc.Str(stripped)
    end
    el.content = inlines
  end

  -- Update last_heading for table caption fallback
  last_heading = pandoc.utils.stringify(el)
  return el
end

-- Make the title page H1 unnumbered (it's the report title, not a chapter)
function Div(el)
  return el
end

-- ── Figure caption: LaTeX provides "图 N" prefix, we provide descriptive text ──
function Figure(el)
  -- The alt text from markdown ![alt](path) → pandoc Figure caption.
  -- LaTeX auto-numbers with "图 N", so we keep only the descriptive text.
  if el.caption and el.caption.long and #el.caption.long > 0 then
    -- Keep existing caption text as-is (from markdown alt or : caption)
    -- LaTeX will prefix with "图 N"
  end
  return el
end

-- ── Table caption: LaTeX provides "表 N" prefix, we provide descriptive text ──
function Table(el)
  local cap_text = ""
  if el.caption and el.caption.long and #el.caption.long > 0 then
    -- Use caption from markdown ": caption" line as-is
    cap_text = pandoc.utils.stringify(el.caption)
  elseif last_heading ~= "" then
    cap_text = last_heading
  end
  if #cap_text > 0 then
    el.caption = pandoc.Caption(pandoc.Plain({pandoc.Str(cap_text)}))
  end
  last_heading = ""

  -- Red header text
  if el.head and el.head.rows then
    for _, row in ipairs(el.head.rows) do
      for _, cell in ipairs(row.cells) do
        if cell.contents and #cell.contents > 0 then
          table.insert(cell.contents, 1,
            pandoc.RawInline('latex', '\\color{hsbcred}'))
        end
      end
    end
  end
  return el
end

return {
  {Header = Header},
  {Figure = Figure},
  {Table = Table}
}
