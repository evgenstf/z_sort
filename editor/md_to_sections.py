def main():
    import argparse
    import os
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('process', args.path)

    with open(args.path, 'r') as md_file:
        content = md_file.read().split("\n\n")


        json_content = []
        json_content.append({"type":"tldr", "content":content[0]})
        for i in range(1, len(content)):
            json_content.append({"type":"markdown", "content":content[i]})

        with open('/'.join(args.path.split('/')[:-1]) + '/sections.json', 'w', encoding='utf-8') as sections_file:
            sections_file.write(json.dumps(json_content, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
