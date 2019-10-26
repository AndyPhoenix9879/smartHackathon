<template>
  <div class="container">
    <h1> <b>List of Accidents</b> </h1>
      <div class="content">
        <div class="tabs">
          tab
        </div>
      </div>
  </div>
</template>

<script>
import jsondata from '../../../../car.json'
export default {
  data () {
    return {
      jsondata
    }
  },
  method: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  border-radius: 15px;
  background-color: #F2F6FC;
  height: 650px;
  width: 750px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0px 0px 25px 0px rgba(82, 99, 175, 0.274);
}

.content {
  margin: 10px; 
  border-radius: 15px;
  background-color: white;
  height: 535px;
  width: 680px;
  position: absolute;
  top: 54%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.tabs {
  padding: 10px;
  box-shadow: 0 0 2px 0 rgba(144,147,153,0.5);
  margin: 15px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
