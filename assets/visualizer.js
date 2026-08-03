/* Shared engine behind every sorting visualization.
 *
 * Each algorithm page supplies a `run` function that drives the animation
 * through the context object below; everything else - rendering, controls,
 * speed, stats, theming - is handled here so the pages stay small and
 * behave identically.
 */

(function () {
    'use strict';

    var THEME_KEY = 'sorting-algorithms-theme';

    /* ---------------- Theme ---------------- */

    function applyTheme(theme) {
        if (theme === 'light' || theme === 'dark') {
            document.documentElement.setAttribute('data-theme', theme);
        } else {
            document.documentElement.removeAttribute('data-theme');
        }
    }

    function currentTheme() {
        var stored = document.documentElement.getAttribute('data-theme');
        if (stored) return stored;
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }

    function initTheme() {
        var toggle = document.getElementById('themeToggle');
        if (!toggle) return;

        toggle.addEventListener('click', function () {
            var next = currentTheme() === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try {
                localStorage.setItem(THEME_KEY, next);
            } catch (error) {
                /* Private browsing blocks storage; the toggle still works for this page. */
            }
            toggle.setAttribute('aria-label', 'Switch to ' + (next === 'dark' ? 'light' : 'dark') + ' theme');
        });
    }

    /* ---------------- Visualizer ---------------- */

    function createVisualizer(config) {
        var container = document.getElementById('arrayContainer');
        var stepsDiv = document.getElementById('steps');
        var startBtn = document.getElementById('startBtn');
        var generateBtn = document.getElementById('generateBtn');
        var speedBtn = document.getElementById('speedBtn');
        var auxPanel = document.getElementById('auxPanel');
        var auxTitle = document.getElementById('auxTitle');
        var auxRow = document.getElementById('auxRow');

        var SPEEDS = [
            { level: 1, label: 'Speed: Slow (x1)' },
            { level: 2, label: 'Speed: Normal (x2)' },
            { level: 4, label: 'Speed: Fast (x4)' }
        ];

        var speedIndex = 0;
        var isAnimating = false;
        var arr = [];

        var randomLength = config.randomLength || 8;
        var randomMin = config.randomMin === undefined ? 10 : config.randomMin;
        var randomMax = config.randomMax === undefined ? 99 : config.randomMax;

        /* ---- rendering ---- */

        function render() {
            container.innerHTML = '';
            arr.forEach(function (value, index) {
                var cell = document.createElement('div');
                cell.className = 'array-element default';
                cell.id = 'elem' + index;
                cell.textContent = value;
                container.appendChild(cell);
            });
        }

        function element(index) {
            return document.getElementById('elem' + index);
        }

        function resetStats() {
            (config.stats || []).forEach(function (stat) {
                var node = document.getElementById(stat.id);
                if (node) node.textContent = stat.initial === undefined ? '0' : stat.initial;
            });
        }

        function sleep(ms) {
            var level = SPEEDS[speedIndex].level;
            return new Promise(function (resolve) {
                setTimeout(resolve, ms / level);
            });
        }

        /* ---- context handed to each algorithm ---- */

        var ctx = {
            get arr() { return arr; },
            get length() { return arr.length; },

            sleep: sleep,

            setClass: function (index, className) {
                var node = element(index);
                if (node) node.className = 'array-element ' + className;
            },

            setRange: function (from, to, className) {
                for (var i = from; i <= to; i++) ctx.setClass(i, className);
            },

            setAll: function (className) {
                ctx.setRange(0, arr.length - 1, className);
            },

            setValue: function (index, value) {
                arr[index] = value;
                var node = element(index);
                if (node) node.textContent = value;
            },

            swap: function (i, j) {
                var temp = arr[i];
                ctx.setValue(i, arr[j]);
                ctx.setValue(j, temp);
            },

            tag: function (index, text) {
                var node = element(index);
                if (!node) return;
                ctx.untag(index);
                var label = document.createElement('span');
                label.className = 'tag';
                label.textContent = text;
                node.appendChild(label);
            },

            untag: function (index) {
                var node = element(index);
                if (!node) return;
                var existing = node.querySelector('.tag');
                if (existing) existing.remove();
            },

            clearTags: function () {
                container.querySelectorAll('.tag').forEach(function (node) {
                    node.remove();
                });
            },

            stat: function (id, value) {
                var node = document.getElementById(id);
                if (node) node.textContent = value;
            },

            bump: function (id) {
                var node = document.getElementById(id);
                if (!node) return 0;
                var next = (parseInt(node.textContent, 10) || 0) + 1;
                node.textContent = next;
                return next;
            },

            max: function (id, value) {
                var node = document.getElementById(id);
                if (!node) return;
                if (value > (parseInt(node.textContent, 10) || 0)) node.textContent = value;
            },

            say: function (html) {
                stepsDiv.innerHTML = html;
            },

            /* Secondary display for counts, buckets and heap levels. */
            aux: function (title, cells) {
                if (!auxPanel) return;
                auxTitle.textContent = title;
                auxRow.innerHTML = '';
                cells.forEach(function (cell) {
                    var node = document.createElement('div');
                    node.className = 'aux-cell' + (cell.highlight ? ' highlight' : '');
                    node.innerHTML =
                        '<span class="aux-key">' + cell.key + '</span>' +
                        '<span class="aux-val">' + cell.val + '</span>';
                    auxRow.appendChild(node);
                });
                auxPanel.classList.add('visible');
            },

            hideAux: function () {
                if (auxPanel) auxPanel.classList.remove('visible');
            }
        };

        /* ---- data ---- */

        function loadExample() {
            arr = (config.defaultExample || [5, 3, 8, 1, 4]).slice();
            render();
            resetStats();
            ctx.hideAux();
            ctx.say(
                'Example with ' + arr.length + ' elements: [' + arr.join(', ') + ']<br>' +
                "Press <strong>Start Animation</strong> to step through it."
            );
        }

        function loadRandom() {
            var span = randomMax - randomMin + 1;
            arr = Array.from({ length: randomLength }, function () {
                return Math.floor(Math.random() * span) + randomMin;
            });
            render();
            resetStats();
            ctx.hideAux();
            ctx.say(
                'New example with ' + arr.length + ' elements: [' + arr.join(', ') + ']<br>' +
                "Press <strong>Start Animation</strong> to step through it."
            );
        }

        /* ---- run loop ---- */

        async function start() {
            if (isAnimating) return;

            isAnimating = true;
            startBtn.disabled = true;
            generateBtn.disabled = true;
            startBtn.textContent = 'Sorting...';

            resetStats();
            ctx.clearTags();
            ctx.setAll('default');
            ctx.say('<strong>Starting.</strong> The array is unsorted.');
            await sleep(1200);

            await config.run(ctx);

            ctx.clearTags();
            for (var i = 0; i < arr.length; i++) {
                ctx.setClass(i, 'sorted');
                await sleep(180);
            }

            ctx.say(
                '<strong>Done.</strong> The array is fully sorted: [' + arr.join(', ') + ']' +
                (config.summary ? '<br><br>' + config.summary(ctx) : '')
            );

            isAnimating = false;
            startBtn.disabled = false;
            generateBtn.disabled = false;
            startBtn.textContent = 'Start Animation';
        }

        speedBtn.textContent = SPEEDS[speedIndex].label;
        speedBtn.addEventListener('click', function () {
            speedIndex = (speedIndex + 1) % SPEEDS.length;
            speedBtn.textContent = SPEEDS[speedIndex].label;
        });

        generateBtn.addEventListener('click', loadRandom);
        startBtn.addEventListener('click', start);

        loadExample();

        return { start: start, loadRandom: loadRandom, loadExample: loadExample, ctx: ctx };
    }

    window.SortingVisualizer = {
        initTheme: initTheme,
        create: createVisualizer
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
})();
