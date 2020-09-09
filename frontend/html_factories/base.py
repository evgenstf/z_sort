
HEADER = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <title>NlogN</title>
  <meta name="description" content="NlogN">
  <meta name="author" content="evgenstf">
</head>

<body>
  <table width=100%>
    <tr>
      <td>
        <div style="padding:5px;background:black;text-align:center;color:white;font-size:20pt">
          NlogN
        </div>
      </td>
    </tr>
    <tr>
      <td>
        {}
      </td>
    </tr>
  </table>
</body>
</html>
"""



class BaseHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content):
        return HEADER.format(content)
