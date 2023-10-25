import random
"""
    Teaches and tests as per content weights. 
    Retests weak lessons every alternate lessons. 
    Clears all weak lessons before moving to next chapter.
"""
syllabus = [['lesson '+str(i) for i in range(10)] for i in range(3)] #sample: 3 chapters of 10 lessons each
content_types = ['text', 'audio'] 
weights= [0.5, 0.5] #chance of each content type, given by the test administered during signup

print("starting simulation")
#simulating the flow of the chapters
for i in syllabus:
    scores = dict() #history of all lessons and their scores
    w_lessons=[] #2d array with weak lessons and their scores, always sorted by decreasing score
    a_chance = 0 #value dictates chance of assessment of older lessons with lower score
    print("Starting chapter:")
    #simulating flow of chapters
    for j in i:
        style = random.choices(content_types, weights)[0]
        
        if a_chance == 1 and w_lessons!=[]:
            testing_lesson = w_lessons[-1][0] #tests weakest lesson first
            print("Retroactive assessment: ",testing_lesson) 
            k = int(input("Assessment score (out of 10): "))
            #if test scores above 8, user is thorough, so remove it from retroactive testing, else keep it with the updated score
            if k>=8: 
                scores[testing_lesson] = k
                w_lessons.pop()
            else:
                if k>=4: print("re-teaching this lesson")
                w_lessons[-1] = [testing_lesson, k]
                w_lessons = sorted(w_lessons, key=lambda x: x[1], reverse=True)
                scores[testing_lesson] = k
        
        print(j,"administered. Content type: ", style)
        k = int(input("Assessment score (out of 10): ")) #one assessment after each lesson, type as per ratio7
        if  k<=7: 
            w_lessons.append([j,k])
            w_lessons = sorted(w_lessons, key=lambda x: x[1], reverse=True)
        scores[j] = k
        a_chance = (a_chance+1)%2
        
    print("chapter complete. current weak lessons:")
    for i,j in w_lessons:
        print(i,"score: ",j)
    print("\n")
    print("Strengthening weak lessons")
    while w_lessons!=[]:
        testing_lesson = w_lessons[-1][0] #tests weakest lesson first
        print("Retroactive assessment: ",testing_lesson) 
        k = int(input("Assessment score (out of 10): "))
        #if test scores above 8, user is thorough, so remove it from retroactive testing, else keep it with the updated score
        if k>=8: 
                scores[testing_lesson] = k
                w_lessons.pop()
        else:
            if k>=4: print("re-teaching this lesson")
            w_lessons[-1] = [testing_lesson, k]
            w_lessons = sorted(w_lessons, key=lambda x: x[1], reverse=True)
            scores[testing_lesson] = k
        
    
    print("Chapter complete. Final scores:")
    for i,j in scores.items():
        print(i,"score: ",j)
    print("\n")
        
    
