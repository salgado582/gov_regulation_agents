<!-- src/views/UploadRules.vue -->
<template>
  <div>
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-lg">
      <h2 class="text-2xl font-bold mb-4">Upload Department Rules</h2>
      <p class="mb-4">
        Upload your department rules file (PDF or TXT) to train the AI.
      </p>
      <input
        type="file"
        @change="handleFileUpload"
        accept=".pdf,.txt"
        class="mb-4  py-2 px-2 rounded bg-gray-300 mr-16 w-[250px]"
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
  </div>
</template>

<script>
import axios from "axios"; // Import Axios
export default {
  name: "UploadRules",
  data() {
    return {
      selectedFile: null,
      uploadStatus: "",
      utcDate: this.getUTCDate(),
      textFile: "Subject: Appeal for Improvement of Power and Water Supply Infrastructure Dear Mrs. Nomsa Khumalo, I am writing to highlight the recurring issues with our school’s power and water supply. Frequent power outages and an inconsistent water supply have adversely affected the learning environment and daily operations. As per the regulations, every school must have access to a reliable power supply (Regulation 10) and a sufficient water supply (Regulation 11) that meets all relevant legal and functional requirements. I urge the relevant authorities to conduct a thorough review and expedite necessary interventions to bring our infrastructure in line with these essential standards. Thank you for your immediate attention to this critical matter. Yours faithfully, Mr. Thabo Mokoena Operations Manager Lakeside Community School"

    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    async uploadFile() {
      if (!this.selectedFile) {
        alert("Please select a file to upload.");
        return;
      }
      this.uploadStatus = "Uploading...";
      // API call.
      try {
        const response = await axios.post("http://localhost:5000/auditing", {
          data: {name: "Test1", text: this.textFile,  date: this.utcDate},
        });

        console.log("Server Response:", response.data);
      } catch (error) {
        console.error("Error sending document:", error);
      }
      setTimeout(() => {
        this.uploadStatus = "Upload complete! AI Training in progress...";
      }, 1500);
    },
    getUTCDate() {
      return new Date().toISOString(); // Returns ISO format in UTC
    }
  },
};
</script>
