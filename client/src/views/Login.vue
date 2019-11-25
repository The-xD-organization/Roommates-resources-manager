<template>
    <login-layout>
        <div class="home">
             <form>
                <input type="text"><br>
                <input type="password"><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </login-layout>
</template>

<script>
import LoginLayout from '@/components/layouts/LoginLayout.vue';

export default {
    name: 'login',
    components: {
        LoginLayout,
    },
};
</script>
