from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # رفتن به سایت گوگل
    page.goto("https://www.google.com")
    
    # چک کردن اینکه عنوان صفحه درست باشد
    expect(page).to_have_title("Google")
    
    print("تست با موفقیت انجام شد!")