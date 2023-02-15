import os
from IPython.display import HTML, display


def create_folder(folder_name):
    """ Make directory if it doesn't already exist """
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name) 
        
        
def display_image(ds):
    """ display image with text
    
    Parameters:
       ds (series): entire row from twitter_archive_master.csv for the tweet we want to print a profile card for
    
    """

    # if an image breed prediction image is available use that as profile picture by default, 
    # otherwise use image downloaded from API
    file_name = ''
    if ds.jpg_url:
        file_name = ds.jpg_url
    else:
        file_name = '../data/image_profiles/' + str(ds.tweet_id) + '.jpg'
     
    name_text = ''
    if (ds['name'] == 'unknown') & (ds['annotation'] != ''):
        name_text = ds['annotation']
    else:
        name_text = ds['name']
        
    breed_text = ''
    if (ds['breed'] == 'unknown') & (ds['annotation'] != ''):
        breed_text = ds['annotation']
    else:
        breed_text = ds['breed']

    if file_name:
        display(HTML(f"""
            <p>
                <img src={file_name} alt={ds['tweet_id']} width=300 style="float:left">
                <h4>{ds['cleantext']}</h4><br>
                <em>Name: {name_text}</em><br>
                <em>Breed: {breed_text}</em><br>    
                <em>Dog stage: {ds['dog_stage']}</em><br>                 
                <em>Score: {ds['rating_numerator']}/{ds['rating_denominator']}</em><br>
                <em>Likes : {ds['like_count']}</em><br>    
                <em>Retweets : {ds['retweet_count']}</em><br>  
                <em><a href={ds['short_url']}>{ds['short_url']}</a></em>
            </p>

            """))
