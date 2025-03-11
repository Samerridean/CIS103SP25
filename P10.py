def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    

# ---------------------------------
    RS=thetext.strip()
    print(RS)
    OL=len(thetext)
    f=thetext.find('the')
    print('\n','Original Text Length:',OL)
    if thetext.find('little'):
        print('\n','Little present?','\n','Yes Little was Found')
    else:
        print('\n','Little present?','\n','No Little was found')
    L=len(RS)
    print('\n','New Text Length:',L)
    print('\n','"The" Count:',f)
    if thetext.find('titan'):
        print('\n','Any Titans About?','\n','Titan was found. RUN!')
    else:
        print('\n','Titan was not found. You are safe.')
    
# ---------------------------------
main()
