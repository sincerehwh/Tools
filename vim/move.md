
光标移动快捷键：


┌──────────────────┐                                      
│   Full Text      │                                      
├──────────────────┤                                      
│       │   ▲      │◀─────gg: Full Text first line (= 1G) 
│◀────  │   │ ────▶│                                      
│       ▼   │      │                                      
│  h    j   k   l  │◀─────C+f: Forward One Page           
│                  │                                      
│                  │◀─────C+b: Back One page              
│                  │                                      
│     Page One     │◀─────C+u: Up half Page               
│                  │                                      
│                  │◀─────C+d: Down half Page             
│                  │                                      
│                  │                                      
├──────────────────┤                                      
│                  │◀─────H: This screen first line       
│                  │                                      
│  Current Screen  │◀─────M: This screen middle line      
│                  │                                      
│                  │◀─────L: This screen last line        
│                  │                                      
├──────────────────┤                                      
│                  │◀─────┬──────────────┐                
│      ......      │      │  n <Enter>   │                
│                  │      │ down n lines │                
│                  │◀─────┴──────────────┘                
├──────────────────┤                                      
│                  │                                      
│     Page End     │                                      
i│                  │◀─────nG: Full Text n Line            
│                  │                                      
└──────────────────┘◀─────G: Full Text END                
                                                          
                                                          
                                                                                         
┌─────────────────────────────────────────────┐           
│                                             │           
│0:Line first char            Line last char:$│           
│                                             │           
└──────────▲───────────────▲──────────────────┘           
           │               │                              
           ├───────────────┤                              
           │n<space> n char│                              
           └───────────────┘                              


搜索：

/words: 向下搜索词

?words: 向上搜索词

n 执行上一次的搜索操作

N 执行上一次的反向操作

:n1,n2 s/word1/word2/g   n1,n2间的词: word2替换word1
:0,$ s/word1/word2/g 	 0,结尾：word2替换word1
:n1,n2 s/word1/word2/gc  每次替换都提示

