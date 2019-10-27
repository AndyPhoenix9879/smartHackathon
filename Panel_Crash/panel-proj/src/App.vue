<template>
  <div id="app">
    <div id="nav">
      <b>Swish Real-Time Emergency Notification System</b>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  color: white;
  padding: 20px;
  background-color: #303133;
  box-shadow: 0px 8px 6px -2px rgba(0, 0, 0, 0.5);
  position: sticky;
  position:-webkit-sticky;
}
</style>
