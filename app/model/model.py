from keybert import KeyBERT

kw_model = KeyBERT()

def get_keywords(text1, text2):
    keywords = kw_model.extract_keywords([text1,text2], keyphrase_ngram_range=(0, 2), stop_words='english', use_mmr=True, diversity=0.5)
    return keywords



if __name__ == "__main__":
    t1 = '<p> Brian Cannon, 44, was charged with three counts of arson and is currently being held at the Salem County Correctional Facility while he awaits a detention hearing, according to police.</p> <p> Just before 7 a.m. Saturday, West Deptford police and fire crews responded to the Colonial Manor United Methodist Church for a report of a building fire, officials said. Upon arrival, police said they found a fire blazing inside the church.</p> <p> Crews from the Woodbury Fire Department, Westville Fire Department, Mantua Fire Department and Deptford Fire Department also responded to the fire scene a'
    t2 = '<p>injuring a number of children and adults, a Michigan sheriff said in a news release.</p> <p> The victims were taken to several area hospitals after the crash that occurred at about 3 p.m. at the Swan Creek Boat Club in Berlin Township, about 30 miles south of Detroit, Monroe County Sheriff Troy Goodnough said.</p> <p> No other details were available.</p>'
    print(get_keywords(t1, t2))
