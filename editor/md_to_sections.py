def main():
    import argparse
    import os
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('process', args.path)

    with open(args.path, 'r') as md_file:
        content = md_file.read()


        json_content = []
        json_content.append({"type":"tldr", "content":content.split("\n\n")[0]})
        json_content.append({"type":"markdown", "content":"\n\n".join(content.split("\n\n")[1:])})

        with open('/'.join(args.path.split('/')[:-1]) + '/sections.json', 'w', encoding='utf-8') as sections_file:
            sections_file.write(json.dumps(json_content, ensure_ascii=False))


if __name__ == '__main__':
    main()
