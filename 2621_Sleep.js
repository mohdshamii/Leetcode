/**
 * @param {number} millis
 * @return {Promise<void>}
 */
async function sleep(millis) {
    return new Promise(resolve => {
        setTimeout(resolve, millis);
    });
}
