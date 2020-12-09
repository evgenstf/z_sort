echo '{"type":"create_article","article_id":"lolkek"}' | nc localhost 9996
echo '{"type":"update_meta","new_meta":{"date":"1 nov 2020","header":["new","header"],"authors":["lolkek"]},"article_id":"lolkek"}' | nc localhost 9996
echo '{"type":"update_sections","new_sections":[{"type":"tldr","content":"updated tldr"},{"type":"markdown","content":"updated content"}],"article_id":"lolkek"}' | nc localhost 9996
echo '{"type":"compile","article_id":"lolkek"}' | nc localhost 9996
