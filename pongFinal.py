import cv2
startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 320

paddleColor = (0,255,0)
paddleX = None
paddleY = None

ballX,ballY = cameraHeight - 12,cameraWidth - 24
ballCordinates = (ballX,ballY)
def createBall(frame,ballCordinates):
    cv2.circle(frame,ballCordinates,3,(255,255,255),25)




class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2):
         self.hands=self.mp.solutions.hands.Hands(False,maxHands)

    def getHands(self,frame):
      myHands = []
      handsType = []
      frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = self.hands.process(frameRGB)
      if results.multi_hand_landmarks != None:
            ##print(results.multi_handedness)
            for hand in results.multi_handedness:
                handedness = hand.classification[0].index
                handsType.append(handedness)

            for handLandMarks in results.multi_hand_landmarks:
                 myHand=[]
                 for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*cameraWidth),int(landMark.y*cameraHeight)))
                 myHands.append(myHand)
                
      return myHands,handsType   

      

def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 





def returnFrame(camera):
      ignore,frame = camera.read()
      frame = cv2.flip(frame, 1)
      return frame


startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    gameWindow = ""
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    font = cv2.FONT_HERSHEY_SIMPLEX
    gameSelectScreen = cv2.imread("pongImgs\Game Mode.png")
    gameSelectScreen = cv2.resize(gameSelectScreen, (640, 320), interpolation=cv2.INTER_LINEAR)
    deathScreen = cv2.imread("pongImgs/You died.png")
    deathScreenRed = cv2.imread("pongImgs/twoPlayerPongDeath.png")
    deathScreenBlue = cv2.cvtColor(deathScreenRed,cv2.COLOR_BGR2RGB)
    handAi = mpHands()
    while True:
        cv2.imshow(gameWindow,gameSelectScreen)
        if cv2.waitKey(1) == ord("q"):
            break
        if cv2.waitKey(1) == ord("1"):
            print("One player")
            ballXRight = True
            ballYUp = True
            lives = 3
            ballSpeed = 10
            paddleWidth = 125
            paddleHeight = 25

            while True:
             frame = returnFrame(camera)
             myHands,handedness = handAi.getHands(frame)
             if ballXRight == True:
               ballX = ballX +  ballSpeed
               ballCordinates = (ballX,ballY)
        
             if ballXRight == False:
              ballX = ballX -  ballSpeed
              ballCordinates = (ballX,ballY)
        
             if ballX >= cameraWidth - 12:
              ballXRight = False

             if ballX <= 12:
              ballXRight = True

             if ballYUp == True:
              ballY += - ballSpeed
              ballCordinates = (ballX,ballY)
        
             if ballYUp == False:
              ballY +=  ballSpeed
              ballCordinates = (ballX,ballY)
        
             if ballY >= cameraHeight + 24:
              ballYUp = True

             if ballY <= 12:
              lives += -1
              ballY = cameraHeight + 24
             if lives == 0: 
               continueSolo = ""
               while True:
                  cv2.imshow(gameWindow,deathScreen)
                  if cv2.waitKey(1) == ord("q"):
                     continueSolo = False
                     break
                  if cv2.waitKey(1) == ord("r"):
                     continueSolo = True
                     lives = 3
                     ballSpeed = 10
                     break
               if continueSolo == False:
                  break
                
             createBall(frame,ballCordinates)
             if myHands != None:
              for hand in myHands:
                 cv2.rectangle(frame,(hand[8][0] - paddleWidth//2 ,0),(hand[8][0] + paddleWidth//2,paddleHeight),paddleColor,-1)
                # Given rectangle parameters
                 rectX = hand[8][0] - paddleWidth // 2  # X-coordinate of the left edge
                 rectY = 24                            # Y-coordinate of the top edge
                 rectWidth = paddleWidth               # Width of the rectangle
                 rectHeight = paddleHeight             # Height of the rectangle

               # Check for collision
                 if rectX <= ballX <= rectX + rectWidth and rectY <= ballY <= rectY + rectHeight:
                  ballYUp = False
                  ballSpeed += 1
             cv2.imshow(gameWindow,frame)
             if cv2.waitKey(1) == ord("q"):
              break
        if cv2.waitKey(1) == ord("2"):
            print("Two player")
            ballXRight = True
            ballYUp = True
            leftHandLife = 5
            rightHandLife = 5
            ballSpeed = 10
            ballX,ballY = cameraHeight - 12,cameraWidth - 24
            ballCordinates = (ballX,ballY)
            paddleWidth = 25
            paddleHeight = 125
            while True:
               frame = returnFrame(camera)
               if ballXRight == True:
                ballX = ballX +  ballSpeed
                ballCordinates = (ballX,ballY)
        
               if ballXRight == False:
                ballX = ballX -  ballSpeed
                ballCordinates = (ballX,ballY)
     
               if ballX >= cameraWidth - 12:
                leftHandLife -= 1
                print(leftHandLife)
                ballXRight = False

               if rightHandLife == 0 and leftHandLife >= 1:
                continueTwoPlayer = ""
                while True:
                  cv2.putText(deathScreenBlue,"left won",(cameraWidth//2 - 50,cameraHeight//2 - 80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
                  ballCordinates = ((cameraWidth//2,cameraHeight//2))
                  cv2.imshow(gameWindow,deathScreenBlue)
                  if cv2.waitKey(1) == ord("q"):
                     continueTwoPlayer = False
                     break
                  if cv2.waitKey(1) == ord("r"):
                     continueTwoPlayer = True
                     leftHandLife = 5
                     rightHandLife = 5
                     ballSpeed = 10
                     break
                if continueTwoPlayer == False:
                  break


               if leftHandLife == 0 and rightHandLife >=1:
                 continueTwoPlayer = ""
                 while True:
                  cv2.putText(deathScreenRed,"right won",(cameraWidth//2 - 50,cameraHeight//2 - 80),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
                  ballCordinates = ((cameraWidth//2,cameraHeight//2))
                  cv2.imshow(gameWindow,deathScreenRed)
                  if cv2.waitKey(1) == ord("q"):
                     continueTwoPlayer = False
                     break
                  if cv2.waitKey(1) == ord("r"):
                     continueTwoPlayer = True
                     leftHandLife = 5
                     rightHandLife = 5
                     ballSpeed = 10
                     break
                 if continueTwoPlayer == False:
                  break

               if ballX <= 12:
                rightHandLife -= 1
                print(rightHandLife)
                ballXRight = True

               if ballYUp == True:
                ballY += - ballSpeed
                ballCordinates = (ballX,ballY)
        
               if ballYUp == False:
                ballY +=  ballSpeed
                ballCordinates = (ballX,ballY)

               if ballY >= cameraHeight + 24:
                ballYUp = True

               if ballY <= 12:
                ballYUp = False

               myHands,handedness= handAi.getHands(frame)
               if myHands != None:
                  for hand,handType in zip(myHands,handedness):
                   if handType == 0 :
                    handcolor = (255,0,0)
                    cv2.rectangle(frame,(cameraWidth ,hand[8][1] - paddleWidth//2),(cameraWidth - paddleWidth, hand[8][1] + paddleHeight),handcolor,-1)
                    rectX1 = cameraWidth - 48
                    rectY1 = hand[8][1] - paddleWidth//2
                    rectX2 = cameraWidth - paddleWidth
                    rectY2 = hand[8][1] + paddleHeight  

                    if rectX1 <= ballX <= rectX2 and rectY1 <= ballY <= rectY2:
                      ballXRight = False
                      ballSpeed += 2


                   else:
                    handcolor = (0,0,255)
                    cv2.rectangle(frame,(0,hand[8][1] - paddleWidth//2),(0 + paddleWidth, hand[8][1] + paddleHeight),handcolor,-1)
                    rectX1 = 0
                    rectY1 = hand[8][1] - paddleWidth//2
                    rectX2 = 16 + paddleWidth
                    rectY2 = hand[8][1] + paddleHeight
             
                    if rectX1 <= ballX <= rectX2 and rectY1 <= ballY <= rectY2:
                     ballXRight = True                              
                     ballSpeed += 2
                   for i in range(20):
                     cv2.circle(frame,hand[i],8,handcolor,2) 
                
               cv2.putText(frame,str(rightHandLife),(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255 ),1)
               cv2.putText(frame,str(leftHandLife),(cameraWidth-20,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0 ),1)
               createBall(frame,ballCordinates)
               cv2.imshow(gameWindow,frame)
               if cv2.waitKey(1) == ord("q"):
                  break
               

            