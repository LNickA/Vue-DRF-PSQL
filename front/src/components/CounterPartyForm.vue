<template>
    <div>
        <h3>Добавление контрагента</h3>
        <form @submit.prevent>
            <div v-show="haveErrors&&this.errors[0]!=null" class="">{{this.errors[0]}}</div>
            <InputUI
              v-model.trim="counterparty.name"
              type="text"
              required
              placeholder="Имя контрагента"/>
            <ButtonUI @click="createCounterParty" class="btn">Создать</ButtonUI>
        </form>
    </div>
</template>
<script>
import ButtonUI from './UI/ButtonUI.vue';
import InputUI from './UI/InputUI.vue';

export default {
    components:{
        InputUI, ButtonUI
    },
    props:{
        id:{
            type: Number,
            required: true,
        }
    },
    data(){
        return{
            counterparty: {
                name:"",
                cost:"Отсутствует",
            },
            haveErrors:false,
            errors:{},
        };
    },
    methods:{
        createCounterParty(){ 
            this.postCounterParty();
            this.haveErrors = true
            console.log(Object.keys(this.errors).length)

        },
        async postCounterParty(){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: this.counterparty.name })
            };
            const response = await fetch("http://127.0.0.1:8000/api/counterparty/", requestOptions);
            const data = await response.json();
            this.errors = data.name
            console.log(this.errors)
            console.log(Object.keys(this.errors).length)
            if (Object.keys(this.errors).length == 0){
                console.log(Object.keys(this.errors).length)
                this.$emit("create", this.counterparty);
                this.counterparty = {         
                    name:'',
                };
            }
            }
        }
    }

</script>
<style scoped>
form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
form>button{
    background-color: #0079C2;
    color: white !important;
}
form>div{
    margin-bottom: 10px;
    color:red
}
h3{margin-bottom: 15px;}
</style>