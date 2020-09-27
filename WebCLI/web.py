#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
mycmd = mydata.getvalue("cmd")

output = subprocess.getoutput("sudo " + mycmd)

print("<html>")
print("""

<head>
    <title> Linux WebCLI </title>
</head>

<style>
body {
    background-color: blue;
    color: red;
    margin: 5;
}

div {
    padding: 10px;
    background-color: green;
}

div h1 {
    text-align: center;
}

div h6 {
    text-indent: 60%;
    display: block;
    padding: 10px;
}

form input{
    left: 30px;
    text-indent: 50%;
}

</style>
<body>

    <div>
        <h1>
            Linux Webies
        </h1>

        <h6> ---Backend RedHat Enterprise Support</h6>

    </div>

    <form action="/cgi-bin/web.py" method="post">
        <label for="cmd">Web Command Line</label>

        <br />
        <input type="text" id="cmd" name="cmd" />

        <br />
        <button type="submit">submit</button>

    </form>


    </form>
""")

print("<pre>")
print(output)
print("</pre>")

print("</body>")
print("</html>")
