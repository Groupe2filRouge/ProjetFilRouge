import markdown

# The service for convertion operations
class ConverterService():

    # Constructor
    def __init__(self):
        print("init ConverterService")

    # Convert local .md file to .html file 
    def convert(self):
        with open('/home/vagrant/tmp/clone/README.md', 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

        with open('/home/shared/tmp/README.html', 'w') as f:
            f.write(html)

        return "document converted"