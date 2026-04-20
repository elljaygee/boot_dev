def create_markdown_image(alt_text):
    text = f"![{alt_text}]"

    def add_url(url):
        url1 = url.replace("(", "%28")
        url2 = url1.replace(")", "%29")
        new_url = f"{text}({url2})"

        def add_title(title=None):
            if title:
                new_title = f'"{title}"'
                mod_url = new_url[:-1]
                final_syntax = f"{mod_url} {new_title})"
                return final_syntax
            else:
                return new_url

        return add_title

    return add_url
