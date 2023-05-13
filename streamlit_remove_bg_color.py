# # We need a few more packages
# from io import BytesIO
# import streamlit as st
# from PIL import Image
# from rembg import remove

# st.title("Hello PY_DEV 🐍 Upload Image!")

# # Upload the file
# image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# # Convert the image to BytesIO so we can download it
# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im

# # If we've uploaded an image, open it and remove the background!
# if image_upload:
#     image = Image.open(image_upload)
#     fixed = remove(image)
#     downloadable_image = convert_image(fixed)
#     st.download_button(
#         "Download fixed image", downloadable_image, "fixed.png", "image/png"
#     )


from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove

st.title("Hello PY_DEV 🐍 Upload Image!")

# Upload the file
image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Convert the image to BytesIO so we can download it!
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# If we've uploaded an image, open it and remove the background!
if image_upload:
    # SHOW the uploaded image!
    st.image(image_upload)
    image = Image.open(image_upload)
    fixed = remove(image)
    downloadable_image = convert_image(fixed)
    # SHOW the improved image!
    st.image(downloadable_image)
    st.download_button(
        "Download fixed image", downloadable_image, "fixed.png", "image/png"
    )


# from io import BytesIO

# import streamlit as st
# from PIL import Image
# from rembg import remove

# st.set_page_config(layout="wide", page_title="Image Background Remover")

# st.write("## Remove background from your image")
# st.write(
#     ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](<https://github.com/tyler-simons/BackgroundRemoval>) on GitHub. Special thanks to the [rembg library](<https://github.com/danielgatis/rembg>) :grin:"
# )
# st.sidebar.write("## Upload and download :gear:")

# # Create the columns
# col1, col2 = st.columns(2)

# # Download the fixed image
# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im

# # Package the transform into a function
# def fix_image(upload):
#     image = Image.open(upload)
#     col1.write("Original Image :camera:")
#     col1.image(image)

#     fixed = remove(image)
#     col2.write("Fixed Image :wrench:")
#     col2.image(fixed)
#     st.sidebar.markdown("\\n")
#     st.sidebar.download_button(
#         "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
#     )

# # Create the file uploader
# my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# # Fix the image!
# if my_upload is not None:
#     fix_image(upload=my_upload)
# else:
#     fix_image("./zebra.jpg")
