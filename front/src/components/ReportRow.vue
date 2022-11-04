<template >
    <tr>
        <td>{{report.score}}</td>
        <td>{{report.volume}}</td>
        <td>{{report.cost}}</td>
    </tr>
</template>
<script>
export default {
    props:{
        report:{
            type:Object,
            required: true,
        }
    }
    
}
</script>
<style scoped>
td{
    text-align: left;
    padding:15px;
  }
td:first-child{
    padding-left: 25px;
  }
</style>