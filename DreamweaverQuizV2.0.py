import random
import os

default_wrong = 10
total_points = 0


questions = {
            'What should you do when links appear to be broken when using the Check Links Site wide command?':  # 1
            [' A) Test the link in a browser \n B) Test the link in live view \n C) Check the File path \n D) View Source Code', 'A'],

            'Which 3 combinations of factors encompass usability?':  # 2
            [' A) Amount of ads,Load time,Window Size \n B) Load Time,Ease of navigation,Efficiency of use \n C) Server download time, \n D) proper Navigation', 'B'],

            'Which line of html code describes a link to an absolute url using the <A> tag and href attribute?':  # 3
            [' A) <A herd = "http://www.acmetoon.org">Acme Toons!</a>, \n B) Herf = "http://www.acmetoon.org">Acme Toons!</a>,'
                '\n C) <A href =http://www.acmetoon.org>Acme toons!</a> \n D) <A herf > = "http://www.acmetoon.org">Acme Toons!</a>', 'C'],

            'Which terms describe a Dreamweaver site that has not been published to a remote server?':  # 4
            [' A) Remote site \n B) local site \n C) local folder \n D) Local File Path', 'B'],

            'Which two files can be imported using the File>Import Command?':  # 5
            [' A) Ms Excel, Ms Word \n B) MS Excel, Video stream \n C) Page, Ms Outlook, \n D) Ms Outlook, Ms Word', 'A'],

            'Choose the right command that will download files from a remote site to the local machine':  # 6
            [' A) Upload-server \n B) Upload to remote server \n C) Update page, \n D) synchronize site wide command', 'D'],

            'What kind of written material can be used without first obtaining copyright permission? ':  # 7
            [' A) Freelance Material  \n B) copyright material \n C) Public Domain Material, \n D) Any open source material', 'C'],

            'How many colors do all browsers recognize?':  # 8
            [' A) 10 \n B) 16 \n C) 20 \n D) 15', 'B'],

            'Select the object or property that screen readers interpret':  # 9
            [' A) Alt Text \n B) Info Text \n C) Source Code \n D) Index Text', 'A'],

            'Choose the view used to display and edit source information created by a third party web design.':  # 10
            [' A) Info View \n B) Split View \n C) Design View  \n D) Code View', 'D'],

            'Where is website content stored on the computer?':  # 11
            [' A) Main Folder \n B) Website Folder \n C) Root Folder  \n D) Info Folder', 'C'],

            'Choose the HTML tag used as an alternative to tables for organizing Web page content.':  # 12
            [' A) <ul> </ul>  \n B) <html> \n C) <herf>  \n D) Div', 'D'],

            'Which Dreamweaver function allows you to create and store content for reuse?':  # 13
            [' A) Save.Match  \n B) Snippets \n C) Reuse  \n D) Store', 'B'],

            'choose which Dreamweaver resource gives example codes for mark up languages programming languages, and CSS styles.':  # 14
            [' A) Mark Code  \n B) Info Text \n C) Info Panel   \n D) Reference Panel', 'D'],

            'Select the rich media file types that can be put in Dreamweaver Files.':  # 15
            [' A) SWF and MOV  \n B) VLC and MOV \n C) DEF and MP4  \n D) MP4 and VLC', 'A'],

            'Select three elements that should appear on a web page design storyboard:':  # 16
            [' A) URL, Wireframe, Image \n B) URL, Navigation, image/drawings  \n C) Wireframe, Image, Color \n D) Color, H1 Text, image', 'B'],

            'which two should be discussed with clients prior to constructing a website?':  # 17
            [' A) Wireframe, Storyboard  \n B) Target Audience, Website cost   \n C) Target Audience, Wireframe \n D) Reference site, Storyboard', 'A'],

            'which statement is true about using material from a sites such as Wikipedia when using a Creative Commons license?':  # 18
            [' A) Provide a full citation using standard style guides. \n B) Material is Public Domain no citation required  \n C) Reference Site \n D) No citation for open source', 'A'],

            'Why is it important to test your site design in multiple browsers?':  # 18
            [' A) To test the speed of the website \n B) To make sure it works on all browsers.  \n C) To view the source code \n D) To view how it looks', 'B'],

            'Which heading style is the largest size?':  # 19
            [' A) H4  \n B) H3  \n C) H2 \n D) H1', 'D'],

            'How can you monitor the effectiveness of a website once it is published?':  # 20
            [' A) Personal Interview , email, Ad Tracking \n B) Personal Interview, mail, ad feedback  \n C) Contact page, email, feedback form, site analytics \n D) None', 'C'],

            'What elements of a page can vary across different browsers?':  # 21
            [' A) Color, layout  \n B) Size, Pictures  \n C) Speed, layout \n D) colors ', 'A'],

            'Choose the tab you would use to insert a navigation bar.':  # 22
            [' A) spry  \n B) data  \n C) common \n D) layout', 'C'],

            'What is the advantage of optimizing images before adding them to a web page?':  # 23
            [' A) Sharpened images  \n B) Improved formatting  \n C) Reduced development time \n D) Reduced download time', 'D'],

            'Choose an attribute that maintains consistency throughout a website:':  # 24
            [' A) Sharpened images  \n B) Protocol layout  \n C) Page Layout \n D) File Size', 'C'],

            'Which element may appear different when displayed in other monitors and browsers?':  # 25
            [' A) Alt Text  \n B) Colors  \n C) Rich Media \n D) Buttons', 'B'],

            'Which two elements are new in HTML5?':  # 26
            [' A) <audio>, <canvas>  \n B) <video> <audio>  \n C) <text> <audio>  \n D) <canvas>, <video>', 'A'],

            'Where do you put the spry assets folder, using the site definition dialog box?':  # 27
            [' A) Window category   \n B) Template category  \n C) Advanced tab \n D) Basic tab', 'C'],

            'Select the text command to emphasize a block quotation.':  # 28
            [' A) Align   \n B) Format text \n C) Indent text \n D) Insert style', 'C'],

            'Find the HTML tag that italicizes text.':  # 29
            [' A) Em   \n B) Tr \n C) Title \n D) Ita', 'A'],

            'Which symbolizes a table cell':  # 30
            [' A) <TD>  \n B) <TR> \n C) <TLE> \n D) <HR>', 'A'],

            'Which of the following is NOT a Hotspot tool?':  # 31
            [' A) Orthogonal Hotspot Tool   \n B) Rectangular Hotspot Tool \n C) Oval Hotspot Tool \n D) Polygon Hotspot Tool', 'A'],

            '_HTML is intended to subsume which two languages?':  # 32
            [' A)<PHP>, <HTML4> \n B) <CSS>,<XHTML>  \n C) <HTML3>, <HTML>  \n D) <XHTML>, <HTML4> ', 'D'],

            '_________ view is a hand-coding environment for writing and editing code.':  # 33
            [' A) Design     \n B) Split  \n C) Code   \n D) Window ', 'C'],

            ' ________ images are used to add texture and interesting color to a Web page.':  # 34
            [' A) Clip Art    \n B) Cropped   \n C) Animated  \n D) Background ', 'D'],

            'A ___________ is a vertical collection of cells in a table.':  # 35
            [' A) Row   \n B) Column   \n C) Table ID  \n D) Table', 'B'],

            'Which graphic format can you Not insert into your web page? ':  # 36
            [' A) bmp    \n B) png  \n C) gif   \n D) You can open all of these ', 'D'],

            'Dreamweaver is sold by what software company:':  # 37
            [' A) Adobe    \n B)  Macromedia  \n C) Microsoft   \n D) No company, the program simply appeared one day on the web. ', 'A'],

            'You can save images for the Web in these formats:':  # 38
            [' A) ftp, fla, jsp   \n B) Flickr  \n C) JPG, GIF, PNG  \n D) PSD, Tiff ', 'C'],

            'What view must you be in on the Files Panel to delete files from on the server':  # 39
            [' A) Testing Server  \n B) Repository View \n C) Remote View  \n D) Local view ', 'C'],

            ' ________________ method is the best choice whenever you need to send a visitor to another site.':  # 40
            [' A) Relative  \n B) Absolute \n C)  Named Anchor  \n D) Internal link ', 'B'],

            ' Which do not update properly?':  # 41
            [' A) Library Items & Templates \n B) Templates & Css Code \n C) Images & Data Type  \n D) All update properly ', 'A'],

            'What is one way to determine whether content is relevant for a website?':  # 42
            [' A) Identify target audience \n B) Make Site Survey \n C) Ask the client  \n D) Title of the site ', 'A'],

            'Which guiding principle will help ensure the accessibility of a website?':  # 43
            [' A) GPAW \n B) WAG \n C) POUR  \n D) PORK ', 'C'],

            'Which practice should be used to most effectively separate content and design?':  # 44
            [' A) Different Web Page \n B) Impeded CCS Repo  \n C) Split View  \n D) External CSS style sheets ', 'D'],

            'Which option is best practice for including animation in a web page?':  # 45
            [' A) Avoid Animations longer than 5s \n B) Increase the amount of moving pictures \n C) Upload tons of animation \n D) None ', 'A'],

            'What does HTML stand for? ':  # 46
            [' A) Hypertext Moving Language \n B) Hypertest Markup Language \n C) Hypertext Markup Language \n D) Hypertext Markup Element', 'C'],

            'design principle examples':  # 48
            [' A) balance, symmetry, repetition \n B) balance, design, borders \n C) design, symmetry, balance \n D) design, borders, balance', 'A'],

            'Tags that appear in the Head content':  # 49
            [' A) <title> <h> <ul> \n B) <link> <meta> <title> \n C) <title> <link> <tb> \n D) <title> <link> <T>', 'B'],

            ' ____ is the process of uploading and downloading files to and from a remote site.':  # 50
            [' A) FTP \n B) Publishing \n C) Pushing \n D) HTTP', 'A'],

}


def run_questions():
    question_number = 0
    wrong_answers = 0
    print()
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for keys in question_keys:
        global total_points
        os.system('cls')
        print('')
        print(keys)
        print(questions[keys][0])
        print()
        question_number += 1
        user_input = input('Enter a letter choice: ')
        user_input = user_input.upper()

        if user_input == questions[keys][1]:          # correct answer
            total_points += 1
            print('Question ' + str(question_number) + '/50')
            print('Total Points: ' + str(total_points))
            print('Correct')
            user = input('Press enter to continue ')
            print()
        elif wrong_answers == default_wrong:            # If 10/10 Wrong
            print()
            print('Game Over')
            print('Question number: ' + str(question_number))
            print('Total Points: ' + str(total_points))
            user = input('press enter for home screen')
            print()
            break
        elif question_number == 50:                        # if 50 correct
            print()
            print("Completed")
            print('question number: ' + str(question_number))
            print("Finale score: ", + str(total_points))
            user = input('press enter for home screen')
            break

        else:
            print('---------------------------')
            print('Wrong')
            print('Question ' + str(question_number) + '/50')
            print('Correct letter was ' + questions[keys][1])
            wrong_answers += 1
            print('Amount wrong ' + str(wrong_answers) + '/' + str(default_wrong))
            print('Total Points: ' + str(total_points))
            print('---------------------------')
            print()
            user = input('Press enter to continue ')
            print()
            print()


def info():
    os.system('cls')
    print()
    print('Instructions:')
    print()
    print('-Read the question and type in a letter A, B, C, or D (can be both lower and uppercase) ')
    print('-If the letter is correct press enter for next question')  # Just call the function Home_screen form here
    print('-If the letter is wrong get one wrong point.')
    print('-If you reach a total of 10 wrong points(10 incorrect question) the program ends')
    print()

    print()
    print('Helpful Videos')
    print()
    print('Dreamweaver certification test video: (Warning bad mic)')
    print('https://www.youtube.com/watch?v=gt7aNunFJN8')
    print('Dreamweaver Tutorial: ')
    print('https://www.youtube.com/watch?v=90-r_h9j3Bs')
    print('https://www.youtube.com/watch?v=lnB9ArvVPXU&list=PLwglS51ddbZEPeURdjLDqFZ4saPGd5EiL')
    print('Learn HTML')
    print('https://www.youtube.com/watch?v=Mp0f0zTPLec&list=PL081AC329706B2953')
    print('https://www.youtube.com/watch?v=kDyJN7qQETA')
    print()

    print()
    print('More practice questions')
    print("https://quizlet.com/74367822/dreamweaver-certification-lesson-1-flash-cards/")
    print("https://quizlet.com/79089279/dreamweaver-certification-2015-flash-cards/")
    print("https://quizlet.com/18255037/dreamweaver-certification-review-flash-cards/")
    print()


    print('Created By: Raul G')
    user_home = input('Press enter for Home Screen')
    home_screen()


def home_screen():

    while True:
        os.system('cls')
        print()
        print('- - - - - - - - - - - - - - - - - - ')
        print('Dreamweaver Practice Test V 2.0')
        print('- - - - - - - - - - - - - - - - - - ')
        print()

        print('Type in a number to select an option: ')
        print('Start Quiz = 1')
        print('More Info = 2')

        user_option = input('number = ')

        if user_option == '1':
            run_questions()
        elif user_option == '2':
            info()
        else:
            print('Unknown key.  Press enter to try again. ')
            enter = input()


home_screen()
