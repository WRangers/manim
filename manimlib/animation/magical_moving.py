from manimlib.animation.composition import LaggedStart
from manimlib.animation.fading import FadeOut
from manimlib.animation.creation import Write
from manimlib.animation.transform import Transform
from manimlib.utils.config_ops import digest_config

NO_OF_CHARS = 256

# BM Algorithm


def badCharHeuristic(string, size):
    ''' 
    The preprocessing function for 
    Boyer Moore's bad character heuristic 
    '''

    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # return initialized list
    return badChar


def search(txt, pat):
    ''' 
    A pattern searching function that uses Bad Character 
    Heuristic of Boyer Moore Algorithm 
    '''
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    index = []

    while(s <= n-m):
        j = m-1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            index.append(s)

            '''	 
				Shift the pattern so that the next character in text 
					aligns with the last occurrence of it in pattern. 
				The condition s+m < n is necessary for the case when 
				pattern occurs at the end of text 
			'''
            s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
        else:
            ''' 
            Shift the pattern so that the bad character in text 
            aligns with the last occurrence of it in pattern. The 
            max function is used to make sure that we get a positive 
            shift. We may get a negative shift if the last occurrence 
            of bad character in pattern is on the right side of the 
            current character. 
            '''
            s += max(1, j-badChar[ord(txt[s+j])])

    return index


class MagicalMove(LaggedStart):
    '''
    You can only apply it to TextMobject() without any LaTex syntax!!!
    '''
    CONFIG = {
        "lag_ratio": 0,
        "run_time": 2,
        "anim_kwargs": {},
        "anim_in_type": Write,
        "anim_out_type": FadeOut,
    }

    def __init__(self, original_text, new_text, **kwargs):
        self.original_text = original_text
        self.new_text = new_text
        digest_config(self, kwargs)
        match_index, index_used = self.string_matching(original_text, new_text)

        anim_group1 = []
        for i, k in zip(self.original_text[0], match_index):
            if k is not -1:
                anim_group1.append(Transform(i, self.new_text[0][k]))
            else:
                anim_group1.append(self.anim_out_type(i))

        anim_group2 = []
        for i, k in enumerate(self.new_text[0]):
            if i in index_used:
                continue
            else:
                anim_group2.append(self.anim_in_type(k))

        anim_group = anim_group1+anim_group2
        super().__init__(*anim_group)

    def string_matching(self, original_text, new_text):
        original = original_text.get_tex_string().replace(' ', '')
        new = new_text.get_tex_string().replace(' ', '')
        index_goto = [-1]*len(original)
        index_used = []

        for k, i in enumerate(original):
            search_index = search(new, i)
            index = [i for i in search_index if i not in index_used]

            if index:
                distances = self.get_distance(k, index)
                min_index = distances.index(min(distances))
                index_goto[k] = index[min_index]
                index_used.append(index[min_index])

        return index_goto, index_used

    def get_distance(self, k, index):
        i_coord = self.original_text[0][k].get_center()
        return [self.get_norm(self.new_text[0][k].get_center(), i_coord) for k in index]

    def get_norm(self, i, i_coord):
        # print('i ', i)
        return sum([abs(k-j)**2 for k, j in zip(i, i_coord)])
