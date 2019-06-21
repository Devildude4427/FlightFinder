import webview


class MainWindow:
    def __init__(self):
        w = webview.WebView(width=1080, height=720, title="Flight Finder",
                            url="https://google.com", resizable=True, debug=False)
        w.run()


if __name__ == "__main__":
    MainWindow()
