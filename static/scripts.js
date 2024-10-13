document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("upload-form");
    const progressContainer = document.getElementById("progress-container");
    const uploadProgress = document.getElementById("upload-progress");
    const progressText = document.getElementById("progress-text");
    const uploadMessage = document.getElementById("upload-message");
    
    if (uploadForm) {
        uploadForm.addEventListener("submit", (event) => {
            event.preventDefault(); // Prevent default form submission
            
            const formData = new FormData(uploadForm);
            const xhr = new XMLHttpRequest();
            xhr.open("POST", uploadForm.action, true);
            
            xhr.upload.onprogress = (event) => {
                if (event.lengthComputable) {
                    const percentComplete = (event.loaded / event.total) * 100;
                    uploadProgress.value = percentComplete;
                    progressText.textContent = `Uploading: ${Math.round(percentComplete)}%`;
                }
            };
            
            xhr.onload = () => {
                if (xhr.status === 200) {
                    progressText.textContent = "Upload complete!";
                    uploadMessage.textContent = "Document uploaded successfully!";
                    uploadMessage.classList.add("success");
                } else {
                    uploadMessage.textContent = "Upload failed. Please try again.";
                    uploadMessage.classList.add("error");
                }
                progressContainer.style.display = "none"; // Hide the progress bar after upload
            };

            xhr.onerror = () => {
                uploadMessage.textContent = "Upload failed. Please try again.";
                uploadMessage.classList.add("error");
                progressContainer.style.display = "none"; // Hide the progress bar if there's an error
            };

            progressContainer.style.display = "block"; // Show the progress bar
            uploadProgress.value = 0; // Reset progress
            xhr.send(formData); // Send the form data
        });
    }
});
