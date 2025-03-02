<template>
  <div class="bg-white p-6 rounded shadow">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Dashboard</h2>
    <h3 class="text-xl font-semibold mb-3">Test PDFs List</h3>
    <ul class="divide-y divide-gray-200">
      <li
        v-for="(pdf, index) in testPDFs"
        :key="index"
        class="py-3 px-2 hover:bg-blue-50 transition-colors"
      >
        {{ pdf }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      testPDFs: ["PDF 1", "PDF 2", "PDF 3"],
    };
  },
};
</script>
