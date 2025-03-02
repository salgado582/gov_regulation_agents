<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-6">Document Auditing</h2>
    <div class="flex flex-col md:flex-row gap-6">
      <!-- Documents List -->
      <div class="md:w-1/3 bg-white p-6 rounded shadow">
        <h3 class="text-2xl font-semibold mb-4">Documents List</h3>
        <ul class="divide-y divide-gray-200">
          <li
            v-for="(doc, index) in documents"
            :key="index"
            @click="selectDocument(doc)"
            :class="[
              'py-3 cursor-pointer transition-colors',
              selectedDocument === doc
                ? 'bg-blue-100 font-semibold'
                : 'hover:bg-blue-50',
            ]"
          >
            {{ doc }}
          </li>
        </ul>
      </div>
      <!-- Document Preview -->
      <div class="md:w-2/3 bg-white p-6 rounded shadow">
        <h3 class="text-2xl font-semibold mb-4">Document Preview</h3>
        <div v-if="selectedDocument">
          <p class="mb-4">
            Preview of <span class="font-bold">{{ selectedDocument }}</span>
          </p>
          <div class="border border-dashed p-6 mb-6">
            [Scanned PDF with highlights]
          </div>
          <div class="bg-yellow-100 border-l-4 border-yellow-500 p-4">
            <p class="font-bold">Flag Explanation:</p>
            <p>Rule XYZ violated</p>
          </div>
        </div>
        <div v-else class="text-gray-600">
          <p>Select a document from the list to preview.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DocumentAuditing",
  data() {
    return {
      documents: ["PDF 1", "PDF 2", "PDF 3"],
      selectedDocument: null,
    };
  },
  methods: {
    selectDocument(doc) {
      this.selectedDocument = doc;
    },
  },
};
</script>
