from collections import deque

def solution(m, musicinfos):
    scales = {
        'C#' : "c",
        'D#' : "d",
        'E#' : "e",
        'F#' : "f",
        'G#' : "g",
        'A#' : "a",
        'B#' : "b"
    }

    def replace_sharp(m):
        notes = ""
        s_count = 0 # "#"의 개수 세기
        for i, note in enumerate(m):
            if note == "#":
                s_count += 1
                notes = notes[:i-s_count] #if i!=1 else ""
                scale = m[i-1]+m[i]
                notes += scales[scale]
            else:
                notes += note
        return notes
    
    def match_score(m, musicinfos):
        result = []
        durations = []

        for idx, info in enumerate(musicinfos):
            score = info.split(',')[3]

            # calculate duration
            end = 60*(int((musicinfos[idx].split(',')[1].split(':'))[0])) + int((musicinfos[idx].split(',')[1].split(':')[1]))
            start = 60*(int((musicinfos[idx].split(',')[0].split(':'))[0])) + int((musicinfos[idx].split(',')[0].split(':')[1]))
            duration = end-start
            durations.append(duration)


            # replace '#'
            m_ = replace_sharp(m)
            score_ = replace_sharp(score)
            

            # play score
            div_mod = divmod(durations[idx], len(score_))
            div = div_mod[0]
            mod = div_mod[1]
            score_played = score_*div + score_[:mod+1]

            
            # rotate played score
            score_ = deque(score_played)
            indices = [i for i, val in enumerate(score_) if val == m_[0]]
            
            for i in indices:
                score_.rotate(-1*i)
                if ''.join(m_) in ''.join(score_):
                    result.append([idx, len(score_played)])
                    break
                else:
                    score_.rotate(i)
                
        return result

    
    if match_score(m, musicinfos) != []:
        answer = sorted(match_score(m, musicinfos), key=lambda x: -x[1])
        ans_idx = answer[0][0]
        answer = musicinfos[ans_idx].split(',')[2]
    else:
        answer = '(None)'
        
    return answer