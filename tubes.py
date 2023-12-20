# Importing necessary libraries
import streamlit as st


# Define a dictionary of movie genres and corresponding movie recommendations with release years
movie_genres = {
    "Action": [
        {"title": "Mencuri Raden Saleh", "year": 2022},
        {"title": "Spiderman : No Way Home", "year": 2021},
        {"title": "Mulan", "year": 2020},
        {"title": "Avengers : End Game", "year": 2019},
        {"title": "Wiro Sableng: Pendekar Kapak Maut Naga Geni 212", "year": 2018},
        {"title": "Guardians of the Galaxy Vol. 2", "year": 2017},
        {"title": "Deadpool", "year": 2016},
        {"title": "Jurassic World", "year": 2015},
        {"title": "The Maze Runner", "year": 2014},
        {"title": "World Waz Z", "year": 2013},
        {"title": "The Avengers", "year": 2012},
        {"title": "The Man from Nowhere", "year": 2010},
    ],
    "Comedy": [
        {"title": "Gara-Gara Warisan", "year": 2022},
        {"title": "Bad Trip", "year": 2021},
        {"title": "Orang Kaya Baru", "year": 2019},
        {"title": "Yowis Ben", "year": 2018},
        {"title": "Susah Sinyal", "year": 2017},
        {"title": "Warkop DKI Reborn: Jangkrik Boss Part 1", "year": 2016},
        {"title": "Comic 8: Casino King Part 1", "year": 2014},
        {"title": "Miracle in Cell No. 7", "year": 2013},
        {"title": "Kapan Kawin", "year": 2015},
        {"title": "Hello Ghost", "year": 2010},  
        {"title": "Bad Boys For Life", "year": 2020},
        {"title": "Get Married 3", "year": 2011},
    ],
    "Drama": [
        {"title": "5CM", "year": 2012},
        {"title": "Alangkah Lucunya (Negeri Ini)", "year": 2010},
        {"title": "Nanti Kita Cerita Tentang Hari Ini", "year": 2020},
        {"title": "Mencari Hilal", "year": 2015},
        {"title": "99 CAHAYA DI LANGIT EROPA", "year": 2013},
        {"title": "Catatan Harian Si Boy", "year": 2011},
        {"title": "Dua Garis Biru", "year": 2019},
        {"title": "Bad and Crazy", "year": 2021},
        {"title": "Hotel King", "year": 2014},
        {"title": "Ada Apa Dengan Cinta 2 ?", "year": 2016},
        {"title": "Life", "year": 2018},
        {"title": "Moammar Emka s : Jakarta Undercover", "year": 2017},
    ],
    "Horor": [
        {"title": "Get Out", "year": 2017},
        {"title": "US", "year": 2019},
        {"title": "A Quiet Place", "year": 2018},
        {"title": "The Babadook", "year": 2014},
        {"title": "Host", "year": 2020},
        {"title": "The Wailing", "year": 2016},
        {"title": "Bedevilled", "year": 2010},
        {"title": "KKN di Desa Penari", "year": 2022},
        {"title": "Villa Nabila", "year": 2015},
        {"title": "Sumpahan Kum Kum", "year": 2012},
        {"title": "Pocong Ngesot", "year": 2011},
        {"title": "MAMA", "year": 2013},
    ],
}

# Define movie posters for each recommendation
movie_posters = {
    #comedy
    "Gara-Gara Warisan": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuT1WgcY8C602pQh_Y7-dtxAaKQ4xEZX96jw&usqp=CAU",
    "Bad Trip": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB0MOt_2I51GVySQ4-3ZJ6PaEaLF5aAdAO_g&usqp=CAU",
    "Orang Kaya Baru": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGat_JfobSi-gfI04LtLW99ZUF5rjz0YZMEA&usqp=CAU",
    "Yowis Ben": "https://m.media-amazon.com/images/M/MV5BMjcwYzU5ZGQtY2I5NC00M2YyLTllZDktZTEzNjdiMWVkMjRkXkEyXkFqcGdeQXVyNzkzODk2Mzc@._V1_.jpg",
    "Susah Sinyal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdrLTBzdw7tMF6QSnD4s8Oe5ZCrt0Iz8Fomw&usqp=CAU",
    "Warkop DKI Reborn: Jangkrik Boss Part 1": "https://upload.wikimedia.org/wikipedia/id/5/55/WDKI_reborn.jpg",
    "Comic 8: Casino King Part 1": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkXBrA7rR47WWVmsRrgF-DVtvmL2HIShK9nA&usqp=CAU",
    "Miracle in Cell No. 7": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6V2Gbvh7EDp7P-PWIVTdTD2eQSTJfzB6jIA&usqp=CAU",
    "Kapan Kawin": "https://upload.wikimedia.org/wikipedia/id/9/92/Kapan-Kawin-Poster-Film-Indonesia.jpg",
    "Hello Ghost": "https://m.media-amazon.com/images/M/MV5BYjZlYTBlZWMtNjc4Ni00ZmEyLTk1ZmQtZGI3ZDg4ZmM2OGU3XkEyXkFqcGdeQXVyNjI4NDY5ODM@._V1_FMjpg_UX1000_.jpg",
    "Bad Boys For Life": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhGSvk9EK6WAe27YBJd4_b9KM_32PkDeF8Yg&usqp=CAU",
    "Get Married 3": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRixM3cOQU8rNhdAg-4lY2Y06U5Yc5a_1dgeA&usqp=CAU",
    #Action
    "Mencuri Raden Saleh": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvwVNWtRqIBlGFrgfaQPIkj_-NYjwZjdwUIgjag2Sn3BbPzfOiL1_v4pQH&s=10",
    "Spiderman : No Way Home": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpniKaKqEWUx3qaY_gvRmbbdbF_peVhtm7pw&usqp=CAU",
    "Mulan": "https://upload.wikimedia.org/wikipedia/id/8/8a/Mulan_2020_film_poster_on_Disney%2B.jpg",
    "Avengers : End Game": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtXZut5ESVlBJtCUmbXLVHHe9PgLHZCFq2mA&usqp=CAU",
    "Wiro Sableng: Pendekar Kapak Maut Naga Geni 212": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFmnNv0gwcfB6_OX3IHzCsAZY8mRmSrNnA9g&usqp=CAU",
    "Guardians of the Galaxy Vol. 2": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtN95CjmJOnT4nHQ6I0cG_VeqGCpHfR-sTbg&usqp=CAU",
    "Deadpool": "https://upload.wikimedia.org/wikipedia/en/2/23/Deadpool_%282016_poster%29.png",
    "Jurassic World": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSreRkuc521LEaFh6608s97SR2Mwpcr0iU23Q&usqp=CAU",
    "The Maze Runner": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwG4bvFn9MGU6SU66ReOYsewc7BDkaYdNGYA&usqp=CAU",
    "World Waz Z": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTa2Y49PgPW7DMC78ZnEW56T1E_S41AROAT_Q&usqp=CAU",
    "The Avengers": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScht8b0F5PKK8pwASyXuBQWB4DNOEzHsMgyA&usqp=CAU",
    "The Man from Nowhere": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRF-Bt3nTMe3tNkh4_I78sc-VPbUw29fpeoA&usqp=CAU",
    #horor
    "Get Out": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/get-out-2017dokblumhouse-productions.jpeg?w=620&q=90",
    "US": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/us-2019-dokuniversal-pictures.png?w=620&q=90",
    "A Quiet Place": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/the-invisible-man-2020dokparamount-pictures.jpeg?w=620&q=90",
    "The Babadook": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/the-babadook2014-dokumbrella-entertainment.jpeg?w=620&q=90",
    "Host": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/dokshadowhouse-films.jpeg?w=620&q=90",
    "The Wailing": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/dok-20th-century-fox.jpeg?w=620&q=90",
    "Bedevilled": "https://akcdn.detik.net.id/community/media/visual/2023/04/14/bedevilled-2010dokprime-video.jpeg?w=620&q=90",
    "KKN di Desa Penari": "https://akcdn.detik.net.id/community/media/visual/2022/10/13/kkn-di-desa-penari-extended_916.jpeg?w=620",
    "Villa Nabila": "https://cdnwpseller.gramedia.net/wp-content/uploads/2023/06/han9.png",
    "Sumpahan Kum Kum": "https://cdnwpseller.gramedia.net/wp-content/uploads/2023/06/han12-204x300.png",
    "Pocong Ngesot": "https://akcdn.detik.net.id/albums/detikhot/artis10/pocongngesot.jpg",
    "MAMA": "https://cdn1-production-images-kly.akamaized.net/9Epuav57zo67pTWbLn9LIlZIldU=/1280x720/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/535234/original/mama-movie-131030b.jpg",
    #Drama
    "5CM": "https://1.bp.blogspot.com/-DPXB5TnEg04/UNLzHviP2RI/AAAAAAAACCk/Q0Nd977htBs/s1600/teaserposterfinal.jpg",
    "Alangkah Lucunya (Negeri Ini)": "https://th.bing.com/th/id/R.8b1a111e4a196120b9475cfd56397ad9?rik=JSJmK7oCsa%2feDA&riu=http%3a%2f%2f3.bp.blogspot.com%2f_LbJZvXH4Zis%2fTO-jw4v6oHI%2fAAAAAAAABsk%2fiflKgr62EAY%2fw1200-h630-p-k-no-nu%2fAlangkah-Lucunya-Negeri-ini.jpg&ehk=4BpB9f1YeFsFxsL0aBkfahvD9Rlmt6m0762NdsL2uiE%3d&risl=&pid=ImgRaw&r=0",
    "Nanti Kita Cerita Tentang Hari Ini": "https://m.media-amazon.com/images/M/MV5BNWQ5MGRiZGItZTFkMS00YTRmLWE1NmMtNDJlYmY3N2E2Y2VmXkEyXkFqcGdeQXVyNzEzNjU1NDg@._V1_UY268_CR16,0,182,268_AL_.jpg",
    "Mencari Hilal": "https://s3.bukalapak.com/img/3262606796/large/index9.jpg",
    "99 CAHAYA DI LANGIT EROPA": "https://th.bing.com/th/id/R.21fa09d45a0715c4891157f1d40ccd8a?rik=6%2bLRL8pMJQsIiA&riu=http%3a%2f%2f2.bp.blogspot.com%2f-FyktodMoZgw%2fUrbX8BWVbQI%2fAAAAAAAAA3s%2f2u6-3bxNRcM%2fs1600%2fposter.jpg&ehk=HV7G19R4XPGOvSLsptWPhW0HrCnFbQubBacGd30JMo0%3d&risl=&pid=ImgRaw&r=0",
    "Catatan Harian Si Boy": "https://akcdn.detik.net.id/albums/detikhot/artis10/catatan.jpg",
    "Dua Garis Biru": "https://assets.kompasiana.com/items/album/2019/07/13/dua-garis-biru-5d2a06800d82307cec628ab2.jpg?t=o&v=555",
    "Bad and Crazy": "https://akcdn.detik.net.id/community/media/visual/2023/05/05/bad-and-crazy-2021doktvn.jpeg?w=620&q=90",
    "Hotel King": "https://akcdn.detik.net.id/community/media/visual/2023/05/05/hotel-king-2014dokmbc.jpeg?w=620&q=90",
    "Ada Apa Dengan Cinta 2 ?": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCeI9XRNVxYw0Fr5egmD3DXOwCzefQqB-3Ixo5LHxFfckD5AJj4cB10zcIPKV2HxZZ_U8&usqp=CAU",
    "Life": "https://akcdn.detik.net.id/community/media/visual/2023/05/05/life-2018dokjtbc.jpeg?w=620&q=90",
    "Moammar Emka s : Jakarta Undercover": "https://yooreka.id/assets/uploads/2017/09/Jakarta-Undercover-poster.jpg"

}


# Define the main function for the Streamlit app
def main():
    if "nama_pengguna" not in st.session_state:
        login_page()
    else:
        welcome_page()
def login_page():
    # Set the title of the web app
    st.title("Movie Recommendation App")
    st.balloons()
    nama_pengguna = st.text_input('Nama Pengguna')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if nama_pengguna == "user" and password == "password":  
            
            st.success(f'Selamat datang, {nama_pengguna}! Anda berhasil login.')
            st.session_state.nama_pengguna = nama_pengguna
            st.rerun()
        else:
            st.error('Login gagal. Mohon periksa kembali nama pengguna dan password.')
def welcome_page():
    # Get user input for movie genre
        selected_genre = st.selectbox("Select a movie genre:", list(movie_genres.keys()))

    # Display the selected genre
        st.write(f"You selected {selected_genre} movies.")

    # Get user input for release year range
        min_year, max_year = st.slider("Select a release year range:", min_value=2010, max_value=2022, value=(2010, 2022))

    # Get movie recommendations from the selected genre within the chosen year range
        recommended_movies = [movie for movie in movie_genres[selected_genre] if min_year <= movie["year"] <= max_year]

    # Display the recommended movies with release years
        st.write(f"We recommend movies released between {min_year} and {max_year}:")
        for movie in recommended_movies:
            title = movie["title"]
            year = movie["year"]
            st.image(movie_posters.get(title, ""), caption=f"{title} ({year})", use_column_width=True)
# Run the Streamlit app
if __name__ == "__main__":
    main()
