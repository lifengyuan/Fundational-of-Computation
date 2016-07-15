#http://www.codeskulptor.org/#user41_j93D5VZP15_0.py
"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = [0] * len(line)
    merged = False

    if len(line) < 2:
        return line

    for indexi in range(0, len(line)):
        if line[indexi] != 0:
            
            for indexl in range(0, len(result)):
               
                if result[indexl] == 0:
                    result[indexl] = line[indexi]
                    merged = False
                    break
                
                elif result[indexl + 1] == 0:
                    
                    if result[indexl] == line[indexi] and merged == False:
                        result[indexl] = result[indexl] + line[indexi]
                        merged = True
                        break
    return result 