import mechanicalsoup


def test_submit_online():
    browser = mechanicalsoup.Browser()
    page = browser.get("https://brickseek.com/walmart-inventory-checker")
    form = mechanicalsoup.Form(page.soup.form)
    form.select_form("")

    input_data = {"zip": "11784","item_id":"9914706"}
    form.input(input_data)

    response = browser.submit(form, page.url)

    # returns the request headers in json format
    json = response.json()
    data = json["form"]
    print(data)

if __name__ == '__main__':
    test_submit_online()
