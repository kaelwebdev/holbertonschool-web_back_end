module.exports = function calculateNumber(type, a, b) {
    const ra = Math.round(a);
    const rb = Math.round(b);
 
    if (type === 'SUM') return ra + rb;

    else if (type === 'SUBTRACT') return ra - rb;

    else if (type === 'DIVIDE')
        return rb === 0 ? 'Error' : ra / rb;
}
