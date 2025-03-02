<!-- src/views/UploadRules.vue -->
<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">Upload Department Rules</h2>
    <p class="mb-4">
      Upload your department rules file (PDF or TXT) to train the AI.
    </p>
    <input
      type="file"
      @change="handleFileUpload"
      accept=".pdf,.txt"
      class="mb-4"
    />
    <button
      @click="uploadFile"
      class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600"
    >
      Upload
    </button>
    <p v-if="uploadStatus" class="mt-4 text-sm text-gray-600">
      {{ uploadStatus }}
    </p>
  </div>
</template>

<script>
export default {
  name: "UploadRules",
  data() {
    return {
      selectedFile: null,
      uploadStatus: "",
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      if (!this.selectedFile) {
        alert("Please select a file to upload.");
        return;
      }
      this.uploadStatus = "Uploading...";
      // Replace with your actual file upload API call.
      setTimeout(() => {
        this.uploadStatus = "Upload complete! AI Training in progress...";
      }, 1500);
    },
  },
};
</script>
