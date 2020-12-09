echo '{"type":"create_article","article_id":"kek"}' | nc localhost 9996
echo '{"type":"update_meta","new_meta":{"date":"1 nov 2020","header":["new","header"],"authors":["kek"]},"article_id":"kek"}' | nc localhost 9996
echo '{"type":"update_sections","new_sections":[{"type":"tldr","content":"updated tldr"},{"type":"markdown","content":"updated content"}],"article_id":"kek"}' | nc localhost 9996
