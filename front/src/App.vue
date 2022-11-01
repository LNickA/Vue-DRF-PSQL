<template >
  <NavBar></NavBar>
  <div class="app">
    <RouterView></RouterView>
  </div>
  <FooterUI></FooterUI>
</template>
<script>
import FooterUI from './components/UI/FooterUI.vue';
import NavBar from './components/UI/NavBar.vue';
    export default {
    components: { NavBar, FooterUI }
}
</script>
<style >
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
@font-face {
	font-family: 'Montserrat';
	src: url('~@/static/fonts/montserrat/Montserrat-Light.woff2') format('woff2') url('~@/static/fonts/montserrat/Montserrat-Light.woff') format('woff');
	font-weight: 300;
	font-style: light;
}
@font-face {
	font-family: 'Montserrat';
	src: url('~@/static/fonts/montserrat/Montserrat-Medium.woff2') format('woff2') url('~@/static/fonts/montserrat/Montserrat-Medium.woff') format('woff');
	font-weight: 500;
	font-style: normal;
}
@font-face {
	font-family: 'Montserrat';
	src: url('~@/static/fonts/montserrat/Montserrat-Bold.woff2') format('woff2') url('~@/static/fonts/montserrat/Montserrat-Bold.woff') format('woff');
	font-weight: 700;
	font-style: bold;
}
.app{
  font-size: 14px;
  line-height: 1.15;
  background-color: #F2F7FC;
  font-family: 'Montserrat', sans-serif;
}
.app>div{
  padding-bottom: 50px;
}
</style>