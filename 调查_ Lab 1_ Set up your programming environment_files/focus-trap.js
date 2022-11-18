"use strict";
eesy.define('focus-trap', ['utils'], function (utils) {
    function createFocusTrapListener(elementWithTrap) {
        return function (event) {
            var target = event.target;
            if (!(target instanceof Element)) {
                return;
            }
            var isInsidePopup = elementWithTrap.contains(target);
            if (isInsidePopup) {
                return;
            }
            var focusableElements = getFocusableElements(elementWithTrap);
            if (!focusableElements.length) {
                return;
            }
            var firstToFocus = focusableElements[0];
            var currentFocus = event.relatedTarget;
            var isNavigatingBack = currentFocus && currentFocus === firstToFocus;
            if (isNavigatingBack) {
                var lastToFocus = focusableElements[focusableElements.length - 1];
                lastToFocus.focus();
            }
            else {
                firstToFocus.focus();
            }
        };
    }
    function createFocusTrap(target) {
        var _a;
        // adding additional focusable elements to make sure focus trap works consistent
        // when target is first or last element of body
        var additionalFocusAfter = document.createElement('span');
        additionalFocusAfter.tabIndex = 0;
        var additionalFocusBefore = additionalFocusAfter.cloneNode();
        target.after(additionalFocusAfter);
        target.before(additionalFocusBefore);
        var focusTrapListener = createFocusTrapListener(target);
        document.addEventListener('focusin', focusTrapListener);
        var removeFocusTrap = function () {
            document.removeEventListener('focusin', focusTrapListener);
            additionalFocusAfter.remove();
            additionalFocusBefore.remove();
        };
        utils.onElementRemove(target, removeFocusTrap);
        (_a = getFocusableElements(target)[0]) === null || _a === void 0 ? void 0 : _a.focus();
        return removeFocusTrap;
    }
    function getFocusableElements(element) {
        var selectors = 'a[href], button, input, textarea, select, details, iframe, [tabindex]:not([tabindex="-1"])';
        var filter = function (el) {
            return !el.hasAttribute('disabled') && !el.getAttribute('aria-hidden') && el.offsetParent !== null;
        };
        return Array.prototype.slice.call(element.querySelectorAll(selectors)).filter(filter);
    }
    return {
        createFocusTrap: createFocusTrap,
    };
});
//# sourceMappingURL=focus-trap.js.map