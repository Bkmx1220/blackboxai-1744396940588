<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-white shadow-sm">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <router-link to="/" class="text-xl font-semibold text-green-600">AgroConnect</router-link>
        <div class="space-x-4">
          <router-link to="/login" class="text-gray-600 hover:text-green-600">Login</router-link>
        </div>
      </div>
    </nav>
    <router-view class="py-8"/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>


<style>
/* Removed redundant styles since we are using Tailwind CSS */
</style>
