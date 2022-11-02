<template>
    <div class="">
        <select v-model="localModelValue" @change="$emit('update:modelValue', $event.target.value)">
            <option
            v-for="option in options"
            :key="option.id"
            :value="option.id"
            >
            {{option.name}}
            </option>
        </select>
    </div>
</template>

<script>
    export default {
        name: 'SelectUI',
        props:{
            modelValue:{
                type:String
            },
            options:{
                type:Array,
                default:()=>[]
            }
        },
        computed: {
            localModelValue: {
                get() {
                    return this.modelValue
                },
                set(newValue) {
                    this.$emit('update:modelValue', newValue)
                },
            },
        },
    }
</script>

<style scoped>
select {
    width: 100%;
    border: 1px solid #ECECEC;
    border-radius: 50px;
    padding: 16px 32px;
    margin-bottom: 15px;
    background: white;
}
select::-ms-expand{
    margin-right: 10px;
}

</style>