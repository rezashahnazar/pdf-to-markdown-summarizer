import os


def save_content_to_markdown_file(
    content: str, path_to_input_file: str, output_dir: str
) -> str:
    try:
        for dir in os.path.join(output_dir).split("/"):
            if not os.path.exists(dir):
                print(f"Creating {dir}")
                os.makedirs(dir)
    except Exception as e:
        print(f"Error saving content to markdown file: {e}")
        raise e

    try:
        file_name = os.path.basename(path_to_input_file).split(".")[0].split("/")[-1]
        path_to_markdown_file = os.path.join(output_dir, f"{file_name}.md")
        with open(path_to_markdown_file, "w") as f:
            f.write(content)
        print(f"Content saved to {path_to_markdown_file}")
        return path_to_markdown_file
    except Exception as e:
        print(f"Error saving content to markdown file: {e}")
        raise e
