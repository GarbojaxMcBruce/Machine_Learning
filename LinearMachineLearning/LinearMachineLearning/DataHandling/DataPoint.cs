using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearMachineLearning.DataHandling
{
    public class DataPoint
    {
        #region Properties
        public int InputSize { get; set; }
        public double[] Input { get; set; }
        public double Output { get; set; }
        #endregion

        #region Constructors
        public DataPoint()
        {
            InputSize = 1;
            Input = new double[InputSize];
            Output = 0;
        }

        public DataPoint(int inputSize)
        {
            InputSize = inputSize;
            Input = new double[InputSize];
            Output = 0;
        }

        public DataPoint(double[] input, double output)
        {
            InputSize = input.Length;
            Input = input;
            Output = output;
        }
        #endregion
    }
}
