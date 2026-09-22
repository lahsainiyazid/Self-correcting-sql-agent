analyst_instructions=f"""
You are tasked with creating a set of AI analyst personas .Follow 
these instructions carefully:
1.First,review research topic :
{topic}
2.Examinate any editorial feedback that has been optionally provided to guide creation of 
        {human_analyst_feedback}
3. Determine the most interesting themes based upon documents and /or feedback above.
4.Pick the top {max_analysts} thems.
5.Assign one analyst to each theme.
    """
