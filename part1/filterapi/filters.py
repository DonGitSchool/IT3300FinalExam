#this class will return a fortune
import hug
import subprocess

@hug.cli()
@hug.get(examples="language=b1ff&plaintext=hello")
@hug.local()
def translate(language: hug.types.text, plaintext: hug.types.text):
    #they should pass in the language they want to translate
    if plaintext == "":
        plaintext = 'This is my sample text'
    cmd = "echo '" + plaintext + "' | /usr/games/" + language 
    #echo "this is my text" | /usr/games/cockney
    result = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE)
    return { "translated":result.stdout }
    #return { "translated":cmd }

@hug.cli()
@hug.get(examples="language=b1ff&plaintext=hello")
@hug.local()
def sample(language: hug.types.text, plaintext: hug.types.text):
    cmd = "echo '" + plaintext + "' | /usr/games/" + language 
    return { "translated":cmd }


if __name__=="__main__":
    translate()
