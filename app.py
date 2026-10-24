
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="EdgeInspect AI",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 EdgeInspect AI")
st.caption(
    "Real-Time Edge-AI Visual Inspection System "
    "for Automated Industrial Defect Detection"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Image Inspection",
        "System Architecture",
        "Project Modules",
        "Project Progress"
    ]
)

if page == "Dashboard":
    st.header("Industrial Quality Inspection Dashboard")
    st.write(
        "A prototype interface for automated surface "
        "defect inspection using Edge AI."
    )

    a, b, c = st.columns(3)
    a.metric("Core Modules", "5")
    b.metric("Dataset", "GC10-DET / NEU-DET")
    c.metric("Model Status", "Not Connected")

    st.info(
        "Current stage: Dashboard and architecture prototype. "
        "AI model training and integration are pending."
    )

elif page == "Image Inspection":
    st.header("Product Image Inspection")

    uploaded = st.file_uploader(
        "Upload an industrial product image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(
            image,
            caption="Uploaded Product Image",
            use_container_width=True
        )
        st.write("Image dimensions:", image.size)
        st.warning(
            "Preview only: no AI model is connected, "
            "so defect detection has not been performed."
        )
    else:
        st.info("Upload an image to preview it here.")

elif page == "System Architecture":
    st.header("System Architecture")

    steps = [
        ("1. Image Acquisition",
         "Capture or upload a product image."),
        ("2. Image Preprocessing",
         "Resize and prepare the image using OpenCV."),
        ("3. AI Defect Detection",
         "A trained YOLO model will locate defects."),
        ("4. Result Analysis",
         "Analyze defect classes and confidence scores."),
        ("5. GUI Dashboard",
         "Display inspection results to the user.")
    ]

    for title, description in steps:
        st.subheader(title)
        st.write(description)
        if title != steps[-1][0]:
            st.markdown("⬇️")

    st.info(
        "Planned extensions: edge optimization and "
        "simulated IoT alerts."
    )

elif page == "Project Modules":
    st.header("Project Modules")

    modules = {
        "Image Acquisition": "Collect industrial product images.",
        "Image Preprocessing": "Prepare images for model inference.",
        "Dataset Preparation": "Organize images and annotations.",
        "AI Defect Detection": "Detect defects using a trained model.",
        "Result Analysis": "Display defect locations and confidence.",
        "Edge Optimization": "Planned model optimization for edge devices.",
        "IoT Alerts": "Planned simulated alerts for detected defects."
    }

    for name, description in modules.items():
        with st.expander(name):
            st.write(description)

elif page == "Project Progress":
    st.header("Project Progress")

    st.write("Dashboard interface")
    st.progress(100)

    st.write("Image upload and preview")
    st.progress(100)

    st.write("AI model training and integration")
    st.progress(0)

    st.write("Edge deployment and IoT integration")
    st.progress(0)

    st.caption(
        "Progress indicators describe prototype features, "
        "not overall project completion percentages."
    )
