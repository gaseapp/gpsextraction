import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def main():
    st.set_page_config(page_title="App", page_icon=":leaf:", layout="wide")
    st.markdown("<h1 style='text-align: center;'>dgdfgdf</h1>", unsafe_allow_html=True)

    # Create a menu with multiple pages
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Home":
        st.write("<p style='text-align: center; font-style: italic;'>"
                 ".</p>", unsafe_allow_html=True)
        st.write("Please upload an image containing the rice field:")

        option = st.radio("", ("Upload", "Camera"))
  
        if option == "Upload":
            st.write("Please drag and drop a photo below:")
            uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                # Read the uploaded file and convert it into an image object
                img = Image.open(uploaded_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

                # Check if the image has Exif data
                if 'exif' in img.info:
                    # Get the Exif data
                    exif_dict = piexif.load(img.info['exif'])
                    
                    # Extract the GPS coordinates
                    gps_latitude = exif_dict["GPS"][piexif.GPSIFD.GPSLatitude]
                    gps_latitude_ref = exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef]
                    gps_longitude = exif_dict["GPS"][piexif.GPSIFD.GPSLongitude]
                    gps_longitude_ref = exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef]
                    
                    # Convert the GPS coordinates to degrees
                    lat = (gps_latitude[0][0] / gps_latitude[0][1] +
                           gps_latitude[1][0] / (60 * gps_latitude[1][1]) +
                           gps_latitude[2][0] / (3600 * gps_latitude[2][1]))
                    
                    if gps_latitude_ref == "S":
                        lat = -lat
                    
                    lon = (gps_longitude[0][0] / gps_longitude[0][1] +
                           gps_longitude[1][0] / (60 * gps_longitude[1][1]) +
                           gps_longitude[2][0] / (3600 * gps_longitude[2][1]))
                    
                    if gps_longitude_ref == "W":
                        lon = -lon
                    
                    st.write(f"Latitude: {lat}, Longitude: {lon}")
                else:
                    st.write("This image does not have Exif data.")
            
        elif option == "Camera":
            st.write("Please drag and drop a photo below:")
            image_file = st.camera_input("")
            if image_file is not None:
                img = Image.open(image_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

                # Check if the image has Exif data
                if 'exif' in img.info:
                    # Get the Exif data
                    exif_dict = piexif.load(img.info['exif'])

                # Extract the EXIF data
            exif_dict = piexif.load(image.info['exif'])

            # Extract the GPS coordinates and convert to decimal degrees
            gps_latitude = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude]
            gps_latitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef]
            gps_longitude = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]
            gps_longitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef]
            gps_altitude = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
            gps_altitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSAltitudeRef]

            lat = (gps_latitude[0][0]/gps_latitude[0][1] +
                   gps_latitude[1][0]/(60*gps_latitude[1][1]) +
                   gps_latitude[2][0]/(3600*gps_latitude[2][1]))
            if gps_latitude_ref == 'S':
                lat = -lat

            lon = (gps_longitude[0][0]/gps_longitude[0][1] +
                   gps_longitude[1][0]/(60*gps_longitude[1][1]) +
                   gps_longitude[2][0]/(3600*gps_longitude[2][1]))
            if gps_longitude_ref == 'W':
                lon = -lon

            alt = (gps_altitude[0]/gps_altitude[1])
            if gps_altitude_ref == 1:
                alt = -alt

            # Extract the UTC time and date
            utc_time = exif_dict['0th'][piexif.ImageIFD.DateTime].decode('utf-8')
            utc_time = datetime.strptime(utc_time, '%Y:%m:%d %H:%M:%S')

            # Display the GPS data and UTC time and date
            st.write(f"Latitude: {lat:.6f}, Longitude: {lon:.6f}, Altitude: {alt:.2f}")
            st.write(f"UTC Time: {utc_time}")


    elif choice == "About":
         st.write("""sdgdfgdgdgfdd
        """)

if __name__ == '__main__':
    main()
