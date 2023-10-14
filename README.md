# Billboard-to-Spotify

This program takes top 100 songs of any date from https://www.billboard.com/ and automatically creates a spotify playlist in your account.

STEPS:
1> First head over to Developer Dashboard (https://developer.spotify.com/dashboard) of Spotify and create a app. \n
2> While creating a app make sure to add "http://example.com" in the Redirect URI field.
3> Head over to the Settings and add your environment variables as SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET with their respective values.
   **note: Its not SPOTIFY, its SPOTIPY
4> Run your program and a new tab will open in your browser which looks like:


![Screenshot 2023-10-14 183529](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/cfa83918-9786-473e-8af2-9958c992ddbb)


5> Click Agree and it will redirect you to :
![Screenshot 2023-10-14 183546](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/a6fc8cdb-19fa-4640-80d4-534abda7b137)


6> Copy the url of the page and paste it in the terminal or console of your program:
![Screenshot 2023-10-14 183623](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/1d7b864a-1607-48b3-b7e3-a4f4af4c6468)


7> In your Directory a new file "token.txt" will be generated:
![Screenshot 2023-10-14 183740](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/bb7a0d4b-030c-4fc0-ab1d-7dc354061fd8)


8> Everything we did untill now was all for authentication purposes and you do not need to do this process again. After this, Everytime the program runs it will look at the token.txt to authenticate.
9> Add a date in correct format:
   **note: Make sure it is in correct format.
![Screenshot 2023-10-14 183935](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/ecb91d2c-61cf-49e0-b8aa-353394132ac5)


10> Done! Wait a few seconds and a new playlist will be created in your spotify account.
![Screenshot 2023-10-14 183913](https://github.com/rishichop/Billboard-to-Spotify/assets/84148892/4c7832db-ade1-448d-9f59-e5558a9bc353)
