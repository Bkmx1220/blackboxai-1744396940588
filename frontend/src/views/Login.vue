<template>
  <div class="container mx-auto p-4 max-w-md">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Login</h2>
    <form class="space-y-4">
      <div>
        <label class="block text-gray-700">Email</label>
        <input type="email" class="w-full px-4 py-2 border rounded-md">
      </div>
      <div>
        <label class="block text-gray-700">Password</label>
        <input type="password" class="w-full px-4 py-2 border rounded-md">
      </div>
      <button type="submit" class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700">
        Login
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView'
}
</script>