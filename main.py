import speech_recognition
import sys, os, re
from textwrap import wrap
allowed_extensions = r"(.*\.wma|.*\.mp3|.*\.flac|.*\.wav)"

def speech_to_text(audiofile:str) -> str:
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile("./input/"+audiofile) as source:
        audio = r.record(source)
        said = r.recognize_google(audio, language="nl_NL")
        return said
       
def get_audiofiles() -> list:
    try:
        files = os.listdir("./input")
    except FileNotFoundError:
        print("No input has been found. Please put your files in the input folder.")
        os.mkdir("./input")
    allowed=[]
    for file in files:
         if re.search(allowed_extensions,file):
            allowed.append(file)
    return allowed

def write_output(parsed:dict[str,str]) -> None:
    with open('output.txt','w') as f:
        for key in parsed:
            f.write(key:+"\n")
            #Get multiline support for long outputs
            splicedstring = wrap(parsed[key], 300)
            for line in splicedstring:
                f.write(line+"\n")

if __name__ == '__main__':
    files = get_audiofiles()
    fileresult = {}
    for file in files:
        fileresult[file] = speech_to_text(file)
    write_output(fileresult)
