<template>
    <form @submit.prevent="onSubmit">
        <input type="text" v-model="char">
        <button type="submit">Find</button>
    </form>
</template>

<script>
    export default {
        data() {
            return {
                char: ''
            }
        },
        methods: {
            onSubmit() {
                if (this.char.trim()) {
                    const newQuery = this.char
                    this.$emit('ask-char', newQuery)
                }
            }
        }
    }
</script>

<style scoped>
    form {
        display: flex;
    }

    input {
        width: 400px;
    }
</style>