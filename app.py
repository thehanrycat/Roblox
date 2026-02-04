COOKIE = ".ROBLOSECURITY = _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhsKBGR1aWQSEzEzNjc5Nzk3NzMzMTAxNDQ5MTAoAw.qHpCsK9IBrEri86_E-aK5tY02f-S6pRitK3h_rG4l-VdexCa0upbAXvdzbd2xWgBZarJMUW3hNKwgQ9iI_EP347mNWv-seukYaLw1EWmndq4tYmnp4NHxf0AFd3g2AX2IGzRyXrM5JzEal1m4bsqZ2JVDNAWXvmYyU7fgPhzpr28E4zWhb9TJnRJEFm0tGQgxXjU6dl5-5Yw2Q9nSOeFnbjY8Z8NFanmmWnG1Zq6zZv3PGyGqxIZ1cmukimVpm39GToKYFsUccIuXwXtxrEX6MFOLb932-QcEOXipUVHg1d6267vAPyDYlHHkPpe0KRY0bd05LstTMUGorG7prHxFOWCZO2Is4_DHCWOkKhX1bzKwPkpzmmDrmf5wQcP2VzUBndgxOk8cCmi-r9f17zhHtJXL5FzmucLHrKdWkq7LaSdvjey7sK3W5SXUUcdNqFsudGzEdp7dCJ6_HnBfw0mxMskONGICC-a9YaeVjCYtEdXcHfOWExmXRi3VHFe2bqzuHvLqbI6BMg699-HN5vN-WDs3ohIDJlI4DfE5m2UijoE34GDGyn_yAyoekCdMhzxgIuIXH_IQdGvZEBJN0h3fMt4aATliCxIKi989FclBBVoXRTkr5YIFE4CREFYsMZJHQOH32PQhXZnxlnCywpKRqqwfOHQdz6IN9oaKDiviJYuHzd7VnEQm8Sfv8PU72CY1jts1WmqUm0AwVp5CK5cNN83IK15-TAHy5tJFRJQlbCRs0hAe_vYRm--BImccmMaETAqIfUntjeZa6VrEEcLszkaiLQlVEJcUow1KRsaY23DPCVt"

import webview
import time

def on_loaded(window):
    time.sleep(1.0)  # give page time to start its own scripts

    js = """
    document.cookie = ".ROBLOSECURITY = _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhsKBGR1aWQSEzEzNjc5Nzk3NzMzMTAxNDQ5MTAoAw.qHpCsK9IBrEri86_E-aK5tY02f-S6pRitK3h_rG4l-VdexCa0upbAXvdzbd2xWgBZarJMUW3hNKwgQ9iI_EP347mNWv-seukYaLw1EWmndq4tYmnp4NHxf0AFd3g2AX2IGzRyXrM5JzEal1m4bsqZ2JVDNAWXvmYyU7fgPhzpr28E4zWhb9TJnRJEFm0tGQgxXjU6dl5-5Yw2Q9nSOeFnbjY8Z8NFanmmWnG1Zq6zZv3PGyGqxIZ1cmukimVpm39GToKYFsUccIuXwXtxrEX6MFOLb932-QcEOXipUVHg1d6267vAPyDYlHHkPpe0KRY0bd05LstTMUGorG7prHxFOWCZO2Is4_DHCWOkKhX1bzKwPkpzmmDrmf5wQcP2VzUBndgxOk8cCmi-r9f17zhHtJXL5FzmucLHrKdWkq7LaSdvjey7sK3W5SXUUcdNqFsudGzEdp7dCJ6_HnBfw0mxMskONGICC-a9YaeVjCYtEdXcHfOWExmXRi3VHFe2bqzuHvLqbI6BMg699-HN5vN-WDs3ohIDJlI4DfE5m2UijoE34GDGyn_yAyoekCdMhzxgIuIXH_IQdGvZEBJN0h3fMt4aATliCxIKi989FclBBVoXRTkr5YIFE4CREFYsMZJHQOH32PQhXZnxlnCywpKRqqwfOHQdz6IN9oaKDiviJYuHzd7VnEQm8Sfv8PU72CY1jts1WmqUm0AwVp5CK5cNN83IK15-TAHy5tJFRJQlbCRs0hAe_vYRm--BImccmMaETAqIfUntjeZa6VrEEcLszkaiLQlVEJcUow1KRsaY23DPCVt; path=/; SameSite=Lax; Secure=false";
    console.log("Cookie set →", document.cookie);
    // location.reload();   // uncomment if needed (forces cookie to be used)
    """
    window.evaluate_js(js)

if __name__ == "__main__":
    window = webview.create_window(
        "Freak",
        "http://roblox.com",   # ← your URL
        width=1200,
        height=800
    )

    window.events.loaded += lambda: on_loaded(window)

    webview.start()