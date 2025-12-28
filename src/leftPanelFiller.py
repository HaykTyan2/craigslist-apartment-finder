def fillPanel(page, leftPanelOptions):
    min_price, max_price, min_bed, max_bed, options = leftPanelOptions

    # ---- PRICE RANGE ----
    min_box = page.locator("div.range-inputs input[placeholder='min']")
    min_box.wait_for(state="visible", timeout=3000)
    min_box.fill("")   # clear first
    min_box.type(str(min_price), delay=200)

    max_box = page.locator("div.range-inputs input[placeholder='max']")
    max_box.fill("")
    max_box.type(str(max_price), delay=90)

    # ---- BEDROOMS ----
    min_bed_box = page.locator("div.widget-line input.small[type='tel'][name='min_bedrooms']")
    min_bed_box.fill("")
    min_bed_box.type(str(min_bed), delay=120)

    max_bed_box = page.locator("div.widget-line input.small[type='tel'][name='max_bedrooms']")
    max_bed_box.fill("")
    max_bed_box.type(str(max_bed), delay=120)

    # ---- OPTIONS ----
    page.locator("input[type='checkbox'][name='pets_cat'][value='1']").check()

    applyButton = page.locator("button[type='button'].bd-button.text-only:has-text('apply')")
    applyButton.click()

    return page
